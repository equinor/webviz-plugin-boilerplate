from typing import Any, Dict, List, Optional, Union

import pandas as pd
import webviz_core_components as wcc
from dash import State, callback
from dash.exceptions import PreventUpdate
from webviz_config import EncodedFile, WebvizPluginABC
from webviz_config.utils import StrEnum
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

    class Ids(StrEnum):
        GRAPH = "graph"
        GRAPH_SETTINGS = "graph-settings"

    def __init__(self, height: str = "86vh") -> None:
        super().__init__()
        self._height = height

        self.add_settings_group(GraphSettings(), PlotViewElement.Ids.GRAPH_SETTINGS)

    def inner_layout(self) -> wcc.Graph:
        return wcc.Graph(
            style={"display": "block", "height": self._height},
            id=self.register_component_unique_id(PlotViewElement.Ids.GRAPH),
            config={
                "responsive": True,
            },
        )

    @staticmethod
    def download_data_df(graph_figure: Dict[str, Any]) -> pd.DataFrame:
        graph_data: Optional[List[Dict[str, Any]]] = graph_figure.get("data", None)
        if not graph_data:
            return "No data present in graph figure"

        x_values = graph_data[0].get("x", None)
        y_values = graph_data[0].get("y", None)
        if x_values is None or y_values is None:
            return f"Missing x or y data: x = {x_values} and y = {y_values}"

        _df = pd.DataFrame(
            columns=["x", "y"],
        )
        _df["x"] = x_values
        _df["y"] = y_values
        return _df

    def compressed_plugin_data(
        self, graph_figure: Dict[str, Any]
    ) -> Union[EncodedFile, str]:
        return WebvizPluginABC.plugin_data_compress(
            [
                {
                    "filename": f"""{
                        self.component_unique_id(PlotViewElement.Ids.GRAPH).to_string()
                    }.csv""",
                    "content": self.download_data_df(graph_figure).to_csv(index=False),
                }
            ]
        )

    def set_callbacks(self) -> None:
        @callback(
            self.view_element_data_output(),
            self.view_element_data_requested(),
            State(
                self.component_unique_id(PlotViewElement.Ids.GRAPH).to_string(),
                "figure",
            ),
        )
        def _download_data(
            data_requested: Union[int, None], graph_figure: Dict[str, Any]
        ) -> Union[EncodedFile, str]:
            if data_requested is None:
                raise PreventUpdate

            return self.compressed_plugin_data(graph_figure)
