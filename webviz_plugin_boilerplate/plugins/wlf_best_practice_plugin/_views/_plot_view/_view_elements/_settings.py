from typing import List

import webviz_core_components as wcc
from dash.development.base_component import Component
from webviz_config.utils import StrEnum
from webviz_config.webviz_plugin_subclasses import SettingsGroupABC

###################################################################
#
# View element level settings are settings specific for one view
# element in a view. These are more specific settings as e.g.
# selection of line color for a graph.
#
###################################################################


class LineColor(StrEnum):
    RED = "red"
    BLUE = "blue"
    GREEN = "green"


class GraphSettings(SettingsGroupABC):
    class Ids(StrEnum):
        RADIO_ITEMS = "radio-items"

    def __init__(self) -> None:
        super().__init__("Line Colors")

    def layout(self) -> List[Component]:
        return [
            wcc.RadioItems(
                id=self.register_component_unique_id(GraphSettings.Ids.RADIO_ITEMS),
                options=[
                    {
                        "label": LineColor.RED,
                        "value": LineColor.RED,
                    },
                    {
                        "label": LineColor.BLUE,
                        "value": LineColor.BLUE,
                    },
                    {
                        "label": LineColor.GREEN,
                        "value": LineColor.GREEN,
                    },
                ],
                value=LineColor.RED,
            ),
        ]
