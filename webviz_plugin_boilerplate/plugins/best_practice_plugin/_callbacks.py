from typing import Callable

from dash import Input, Output, callback, no_update
from dash.exceptions import PreventUpdate

from webviz_plugin_boilerplate._utils._data_model import DataModel

from ._business_logic import create_flipped_data, create_reversed_data
from ._layout import LayoutElements
from ._property_serialization import (
    GraphDataVisualizationOptions,
    GraphFigureBuilder,
    GraphTypeOptions,
)

###########################################################################
#
# Collection of Dash callbacks.
#
# The callback functions should retrieve Dash Inputs and States, utilize
# business logic and props serialization functionality for providing the
# JSON serializable Output for Dash properties callbacks.
#
# The callback Input and States should be converted from JSON serializable
# formats to strongly typed and filtered formats. Furthermore the callback
# can provide the converted arguments to the business logic for retrieving
# data or performing ad-hoc calculations.
#
# Results from the business logic is provided to the props serialization to
# create/build serialized data formats for the JSON serializable callback
# Output.
#
###########################################################################


def plugin_callbacks(get_uuid: Callable, data_model: DataModel):
    @callback(
        Output(get_uuid(LayoutElements.GRAPH), "figure"),
        Input(get_uuid(LayoutElements.GRAPH_SELECTION_DROPDOWN), "value"),
        Input(get_uuid(LayoutElements.GRAPH_TYPE_RADIO_ITEMS), "value"),
        Input(get_uuid(LayoutElements.GRAPH_DATA_VISUALIZATION_RADIO_ITEMS), "value"),
    )
    def _update_graph(
        selected_graph_value: str,
        graph_type_value: str,
        graph_data_visualization_value: str,
    ) -> dict:
        ##################################################################################
        # De-serialize from JSON serializable format to strongly typed and filtered format
        ##################################################################################
        graph_type = GraphTypeOptions(graph_type_value)
        graph_data_visualization = GraphDataVisualizationOptions(
            graph_data_visualization_value
        )
        selected_graph = (
            selected_graph_value
            if selected_graph_value in data_model.data_set().names()
            else None
        )

        ###########################################
        # Prevent update on invalid graph selection
        ###########################################
        if not selected_graph:
            raise PreventUpdate

        ###############################################################
        # Business logic with "strongly typed" and filtered data format
        ###############################################################
        graph_data = data_model.data_set().get_data(selected_graph)
        if graph_data_visualization is GraphDataVisualizationOptions.REVERSED:
            graph_data = create_reversed_data(graph_data)
        elif graph_data_visualization is GraphDataVisualizationOptions.FLIPPED:
            graph_data = create_flipped_data(graph_data)
        elif graph_data_visualization is not GraphDataVisualizationOptions.RAW:
            return no_update

        ###############################################################
        # Create/build prop serialization by use of business logic data
        ###############################################################
        figure_builder = GraphFigureBuilder(graph_type)
        title = (
            f"Title: {graph_type.value} for {selected_graph} with"
            f" {graph_data_visualization.value} data"
        )
        figure_builder.add_graph_title(title)
        figure_builder.add_graph_data(graph_data)
        figure = figure_builder.get_serialized_figure()

        return figure
