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


class TableOrientation(str, Enum):
    ASC = "asc"
    DESC = "desc"


class TableOrientationSelection(SettingsGroupABC):
    class Ids(str, Enum):
        RADIO_ITEMS = "radio-items"

    def __init__(self) -> None:
        super().__init__("Table orientation")

    def layout(self) -> List[Component]:
        return [
            wcc.RadioItems(
                id=self.register_component_unique_id(
                    TableOrientationSelection.Ids.RADIO_ITEMS.value
                ),
                options=[
                    {
                        "label": TableOrientation.ASC.value,
                        "value": TableOrientation.ASC.value,
                    },
                    {
                        "label": TableOrientation.DESC.value,
                        "value": TableOrientation.DESC.value,
                    },
                ],
                value=TableOrientation.ASC.value,
            )
        ]
