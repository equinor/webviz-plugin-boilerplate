from enum import Enum
from typing import List

import webviz_core_components as wcc
from dash.development.base_component import Component
from webviz_config.webviz_plugin_subclasses import SettingsGroupABC

###################################################################
#
# View level settings are settings common for all view elements in
# the view.
#
###################################################################


class TableOrder(str, Enum):
    ASC = "asc"
    DESC = "desc"


class TableOrderSelection(SettingsGroupABC):
    class Ids(str, Enum):
        RADIO_ITEMS = "radio-items"

    def __init__(self) -> None:
        super().__init__("Table order")

    def layout(self) -> List[Component]:
        return [
            wcc.RadioItems(
                id=self.register_component_unique_id(
                    TableOrderSelection.Ids.RADIO_ITEMS.value
                ),
                options=[
                    {
                        "label": str.upper(TableOrder.ASC.value),
                        "value": TableOrder.ASC.value,
                    },
                    {
                        "label": str.upper(TableOrder.DESC.value),
                        "value": TableOrder.DESC.value,
                    },
                ],
                value=TableOrder.ASC.value,
            )
        ]
