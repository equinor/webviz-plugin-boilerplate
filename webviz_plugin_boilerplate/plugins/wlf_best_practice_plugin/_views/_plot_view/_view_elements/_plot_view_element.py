from enum import Enum

import webviz_core_components as wcc
from webviz_config.webviz_plugin_subclasses import ViewElementABC

from ._settings import GraphSettings


class PlotViewElement(ViewElementABC):
    """View element for plot graph

    The view element contains a graph object for showing data,
    and a settings group for the graph object - setting the
    color selection for the graph content.

    `View element content:`
    - Graph object
    - Settings groups:
        - Graph color settings
    """

    class Ids(str, Enum):
        GRAPH = "graph"
        GRAPH_SETTINGS = "graph-settings"

    def __init__(self, height: str = "86vh") -> None:
        super().__init__()
        self._height = height

        self.add_settings_group(
            GraphSettings(), PlotViewElement.Ids.GRAPH_SETTINGS.value
        )

    def inner_layout(self) -> wcc.Graph:
        return wcc.Graph(
            style={"display": "block", "height": self._height},
            id=self.register_component_unique_id(PlotViewElement.Ids.GRAPH.value),
            config={
                "responsive": True,
            },
        )
