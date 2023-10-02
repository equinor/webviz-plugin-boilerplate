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


class GraphTypeOptions(StrEnum):
    """
    Type definition of graph type options

    For de-serialization of graph type selection in callback Input/State
    property.
    """

    LINE_PLOT = "Line plot"
    BAR_CHART = "Bar chart"


class GraphDataVisualizationOptions(StrEnum):
    """
    Type definition of graph data visualization options

    For de-serialization of graph data visualization selection in callback
    Input/State property.
    """

    RAW = "Raw"
    REVERSED = "Reversed"
    FLIPPED = "Flipped"


class GraphTypeSettings(SettingsGroupABC):
    class Ids(StrEnum):
        RADIO_ITEMS = "radio-items"

    def __init__(self) -> None:
        super().__init__("Graph Type")

    def layout(self) -> List[Component]:
        return [
            wcc.RadioItems(
                id=self.register_component_unique_id(GraphTypeSettings.Ids.RADIO_ITEMS),
                options=[
                    {
                        "label": GraphTypeOptions.LINE_PLOT,
                        "value": GraphTypeOptions.LINE_PLOT,
                    },
                    {
                        "label": GraphTypeOptions.BAR_CHART,
                        "value": GraphTypeOptions.BAR_CHART,
                    },
                ],
                value=GraphTypeOptions.LINE_PLOT,
            )
        ]


class GraphDataVisualization(SettingsGroupABC):
    class Ids(StrEnum):
        RADIO_ITEMS = "radio-items"

    def __init__(self) -> None:
        super().__init__("Graph Data Visualization")

    def layout(self) -> List[Component]:
        return [
            wcc.RadioItems(
                id=self.register_component_unique_id(
                    GraphDataVisualization.Ids.RADIO_ITEMS
                ),
                options=[
                    {
                        "label": "Raw data",
                        "value": GraphDataVisualizationOptions.RAW,
                    },
                    {
                        "label": "Reversed data",
                        "value": GraphDataVisualizationOptions.REVERSED,
                    },
                    {
                        "label": "Flipped data",
                        "value": GraphDataVisualizationOptions.FLIPPED,
                    },
                ],
                value=GraphDataVisualizationOptions.RAW,
            )
        ]
