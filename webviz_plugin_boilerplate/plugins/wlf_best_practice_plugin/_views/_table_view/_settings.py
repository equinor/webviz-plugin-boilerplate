from typing import List

import webviz_core_components as wcc
from dash.development.base_component import Component
from webviz_config.utils import StrEnum
from webviz_config.webviz_plugin_subclasses import SettingsGroupABC

###################################################################
#
# View level settings are settings common for all view elements in
# the view.
#
###################################################################


class TableOrder(StrEnum):
    ASC = "asc"
    DESC = "desc"


class TableOrderSelection(SettingsGroupABC):
    class Ids(StrEnum):
        RADIO_ITEMS = "radio-items"

    def __init__(self) -> None:
        super().__init__("Table order")

    def layout(self) -> List[Component]:
        return [
            wcc.RadioItems(
                id=self.register_component_unique_id(
                    TableOrderSelection.Ids.RADIO_ITEMS
                ),
                options=[
                    {
                        "label": str.upper(TableOrder.ASC),
                        "value": TableOrder.ASC,
                    },
                    {
                        "label": str.upper(TableOrder.DESC),
                        "value": TableOrder.DESC,
                    },
                ],
                value=TableOrder.ASC,
            )
        ]
