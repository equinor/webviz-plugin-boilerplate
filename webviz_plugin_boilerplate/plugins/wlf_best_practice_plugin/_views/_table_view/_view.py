import sys
from dataclasses import dataclass
from typing import Dict, List, Tuple, Union

from dash import Input, Output, State, callback
from dash.exceptions import PreventUpdate
from webviz_config import EncodedFile
from webviz_config.utils import StrEnum
from webviz_config.webviz_plugin_subclasses import ViewABC, callback_typecheck

from webviz_plugin_boilerplate._utils._data_model import DataModel, DataNames

from ._settings import TableOrder, TableOrderSelection
from ._utils._business_logic import create_table_data_with_order
from ._utils._property_serialization import TableDataBuilder
from ._view_elements import TableViewElement

if sys.version_info >= (3, 9):
    from typing import Annotated
else:
    from typing_extensions import Annotated


class TableView(ViewABC):
    """
    This view shows the data in a table. Based on selected data name provided
    from plugin through slots Input, the table data is updated.

    The view contains a table view element and settings for the table - where
    the data can be sorted ascending or descending

    `View content:`
    - Table view element
    - Settings groups:
        - Table order selection (ascending or descending)

    `Callback logic:`
    Update table figure based on shared settings and view settings.
    """

    class Ids(StrEnum):
        TABLE = "table"
        TABLE_ORDER_SELECTION = "table-order-selection"

    @dataclass
    class Slots:
        data_name_selector: Annotated[Input, str]

    def __init__(self, data_model: DataModel, slots: Slots) -> None:
        super().__init__("Table View")

        self._data_model = data_model
        self._slots = slots
        self._table_view_element = TableViewElement()

        column = self.add_column()
        column.add_view_element(self._table_view_element, TableView.Ids.TABLE)

        self.add_settings_group(
            TableOrderSelection(), TableView.Ids.TABLE_ORDER_SELECTION
        )

    def set_callbacks(self) -> None:
        @callback(
            Output(
                self.view_element_unique_id(
                    TableView.Ids.TABLE, TableViewElement.Ids.TABLE
                ),
                "data",
            ),
            Output(
                self.view_element_unique_id(
                    TableView.Ids.TABLE, TableViewElement.Ids.TITLE
                ),
                "children",
            ),
            Input(
                self.settings_group_unique_id(
                    TableView.Ids.TABLE_ORDER_SELECTION,
                    TableOrderSelection.Ids.RADIO_ITEMS,
                ),
                "value",
            ),
            self._slots.data_name_selector,
        )
        @callback_typecheck
        def _update_table(
            selected_order: TableOrder, selected_data_name: DataNames
        ) -> Tuple[List[dict], str]:

            ###########################################
            # Prevent update on invalid graph selection
            ###########################################
            if not selected_data_name:
                raise PreventUpdate

            ###############################################################
            # Business logic with "strongly typed" and filtered data format
            ###############################################################
            table_data = self._data_model.data_set().get_data(selected_data_name)
            table_data = create_table_data_with_order(table_data, selected_order)

            ###############################################################
            # Create/build prop serialization by use of business logic data
            ###############################################################
            table_builder = TableDataBuilder()
            table_builder.add_table_data(table_data)

            title = (
                f"Table for {selected_data_name} data structure with"
                f" {selected_order} data"
            )

            return (table_builder.get_serialized_table_data(), title)

        @callback(
            self.view_data_output(),
            self.view_data_requested(),
            State(
                self._table_view_element.component_unique_id(
                    TableViewElement.Ids.TABLE
                ).to_string(),
                "data",
            ),
        )
        def _download_data(
            data_requested: Union[int, None],
            table_data: List[Dict[str, int]],
        ) -> Union[EncodedFile, str]:
            if data_requested is None:
                raise PreventUpdate

            return self._table_view_element.compressed_plugin_data(table_data)
