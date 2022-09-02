from enum import Enum
from typing import Dict, List, Type, Union

import pandas as pd
from dash import State, callback, dash_table, html
from dash.development.base_component import Component
from dash.exceptions import PreventUpdate
from webviz_config import EncodedFile, WebvizPluginABC
from webviz_config.webviz_plugin_subclasses import ViewElementABC


class TableViewElement(ViewElementABC):
    """View element for table

    The view element contains a table object for showing
    data.

    `View element content:`
    - Label for title
    - Table object
    """

    class Ids(str, Enum):
        TABLE = "table"
        TITLE = "title"

    def __init__(self, height: str = "86vh") -> None:
        super().__init__()
        self._height = height

    def inner_layout(self) -> Type[Component]:
        return html.Div(
            children=[
                html.Label(
                    id=self.register_component_unique_id(
                        TableViewElement.Ids.TITLE.value
                    ),
                ),
                dash_table.DataTable(
                    id=self.register_component_unique_id(
                        TableViewElement.Ids.TABLE.value
                    ),
                    columns=[{"id": "x", "name": "X"}, {"id": "y", "name": "Y"}],
                ),
            ]
        )

    @staticmethod
    def download_data_df(table_data: List[Dict[str, int]]) -> pd.DataFrame:
        x_values = []
        y_values = []
        for index, elm in enumerate(table_data):
            _x = elm.get("x", None)
            _y = elm.get("y", None)
            if _x is None:
                raise ValueError(f'No "x" column data in table at index {index}')
            if _y is None:
                raise ValueError(f'No "y" column data in table at index {index}')
            x_values.append(_x)
            y_values.append(_y)

        _df = pd.DataFrame(
            columns=["x", "y"],
        )
        _df["x"] = x_values
        _df["y"] = y_values
        return _df

    def compressed_plugin_data(
        self, table_data: List[Dict[str, int]]
    ) -> Union[EncodedFile, str]:
        return WebvizPluginABC.plugin_data_compress(
            [
                {
                    "filename": f"""{
                        self.component_unique_id(TableViewElement.Ids.TABLE).to_string()
                    }.csv""",
                    "content": self.download_data_df(table_data).to_csv(index=False),
                }
            ]
        )

    def set_callbacks(self) -> None:
        @callback(
            self.view_element_data_output(),
            self.view_element_data_requested(),
            State(
                self.component_unique_id(TableViewElement.Ids.TABLE).to_string(), "data"
            ),
        )
        def _download_data(
            data_requested: Union[int, None], table_data: List[Dict[str, int]]
        ) -> Union[EncodedFile, str]:
            if data_requested is None:
                raise PreventUpdate

            if not table_data:
                return "No data present in table"

            return self.compressed_plugin_data(table_data)
