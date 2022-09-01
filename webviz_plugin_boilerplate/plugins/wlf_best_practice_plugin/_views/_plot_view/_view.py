import sys
from dataclasses import dataclass
from enum import Enum

from dash import Input, Output, callback, no_update
from dash.exceptions import PreventUpdate
from webviz_config.webviz_plugin_subclasses import ViewABC

from webviz_plugin_boilerplate._utils._data_model import DataModel, DataNames

from ._settings import (
    GraphDataVisualization,
    GraphDataVisualizationOptions,
    GraphTypeOptions,
    GraphTypeSettings,
)
from ._utils._business_logic import create_flipped_data, create_reversed_data
from ._utils._property_serialization import GraphFigureBuilder
from ._view_elements import PlotViewElement
from ._view_elements._settings import GraphSettings, LineColor

if sys.version_info >= (3, 9):
    from typing import Annotated
else:
    from typing_extensions import Annotated


class PlotView(ViewABC):
    """
    This view shows the data in a plot. Based on selected data name provided
    from plugin through slots Input, the graph data is updated.

    The view contains a plot view element and settings for the graph - where
    graph type (scatter or bar plot) can be selected, and the visualization of
    the graph data can be changed (raw, flipped or reversed).

    `View content:`
    - Plot view element
    - Settings groups:
        - Graph type selection (scatter plot or bar plot)
        - Data visualization selection (raw, flipped or reversed)

    `Callback logic:`
    Update graph figure based on shared settings, view settings and view element
    settings.
    """

    class Ids(str, Enum):
        PLOT = "plot"

        GRAPH_TYPE_SETTINGS = "graph-type-settings"
        GRAPH_DATA_VISUALIZATION = "graph-data-visualization"

    @dataclass
    class Slots:
        data_name_selector: Annotated[Input, str]

    def __init__(self, data_model: DataModel, slots: Slots) -> None:
        super().__init__("Plot View")

        self._data_model = data_model
        self._slots = slots

        column = self.add_column()
        column.add_view_element(PlotViewElement(), PlotView.Ids.PLOT.value)

        self.add_settings_group(
            GraphTypeSettings(), PlotView.Ids.GRAPH_TYPE_SETTINGS.value
        )
        self.add_settings_group(
            GraphDataVisualization(), PlotView.Ids.GRAPH_DATA_VISUALIZATION.value
        )

    def set_callbacks(self) -> None:
        @callback(
            Output(
                self.view_element_unique_id(
                    PlotView.Ids.PLOT.value, PlotViewElement.Ids.GRAPH.value
                ),
                "figure",
            ),
            self._slots.data_name_selector,
            Input(
                self.settings_group_unique_id(
                    PlotView.Ids.GRAPH_TYPE_SETTINGS.value,
                    GraphTypeSettings.Ids.RADIO_ITEMS.value,
                ),
                "value",
            ),
            Input(
                self.settings_group_unique_id(
                    PlotView.Ids.GRAPH_DATA_VISUALIZATION.value,
                    GraphDataVisualization.Ids.RADIO_ITEMS.value,
                ),
                "value",
            ),
            Input(
                self.view_element(PlotView.Ids.PLOT.value).setting_group_unique_id(
                    PlotViewElement.Ids.GRAPH_SETTINGS.value,
                    GraphSettings.Ids.RADIO_ITEMS.value,
                ),
                "value",
            ),
        )
        def _update_graph(
            selected_data_name_value: str,
            graph_type_value: str,
            graph_data_visualization_value: str,
            color_value: str,
        ) -> dict:
            ##################################################################################
            # De-serialize from JSON serializable format to strongly typed and filtered format
            ##################################################################################
            graph_type = GraphTypeOptions(graph_type_value)
            graph_data_visualization = GraphDataVisualizationOptions(
                graph_data_visualization_value
            )
            selected_data_name = DataNames(selected_data_name_value)
            color = LineColor(color_value)

            ###########################################
            # Prevent update on invalid graph selection
            ###########################################
            if not selected_data_name:
                raise PreventUpdate

            ###############################################################
            # Business logic with "strongly typed" and filtered data format
            ###############################################################
            graph_data = self._data_model.data_set().get_data(selected_data_name)
            if graph_data_visualization is GraphDataVisualizationOptions.REVERSED:
                graph_data = create_reversed_data(graph_data)
            elif graph_data_visualization is GraphDataVisualizationOptions.FLIPPED:
                graph_data = create_flipped_data(graph_data)
            elif graph_data_visualization is not GraphDataVisualizationOptions.RAW:
                return no_update

            ###############################################################
            # Create/build prop serialization by use of business logic data
            ###############################################################
            figure_builder = GraphFigureBuilder(graph_type, line_color=color)
            title = (
                f"{graph_type.value} for {selected_data_name} data collection with"
                f" {graph_data_visualization.value} data"
            )
            figure_builder.add_graph_title(title)
            figure_builder.add_graph_data(graph_data)
            figure = figure_builder.get_serialized_figure()

            return figure
