import plotly.graph_objs as go

from webviz_plugin_boilerplate._utils._data_model import Data

from .._settings import GraphTypeOptions

###################################################################
#
# Property serialization is used to serialize and de-serialize
# Input, State and Output properties in Dash callbacks.
#
# Inputs and States properties can de-serialized, i.e. be converted
# to strongly typed data formats for further use inside callback.
#
# Furthermore the functionality can create/build serialized data
# formats for properties in Dash callback Outputs.
#
# `Example:`
# Callback outputs performs update in the Dash layout element. For
# Dash a layout element could be e.g. a graph figure. The
# serialization retrieves data for graphing, and builds a graph
# figure. The figure can be obtained in the callback functionality
# and be provided as a serialized property format for the data view
# object in the callback Output list.
#
# Dash callback for properties must be JSON serializable.
# In general, Dash properties can only be dash components, strings,
# dictionaries, numbers, None, or lists of those.
#
###################################################################


class GraphFigureBuilder:
    """
    Figure builder for creating/building serializable Output property data
    for the callback.

    Contains functions for adding title, graph data and retrieving the serialized
    data for callback Output property.
    """

    def __init__(self, graph_type: GraphTypeOptions, line_color: str = "red") -> None:
        self._figure = go.Figure()
        self._graph_type = graph_type
        self._line_color = line_color

    def add_graph_title(self, title: str) -> None:
        self._figure.update_layout(title=title)

    def add_graph_data(self, graph_data: Data) -> None:
        trace = None
        if self._graph_type == GraphTypeOptions.LINE_PLOT:
            trace = go.Scatter(
                x=graph_data.x_data(),
                y=graph_data.y_data(),
                mode="lines",
                line_color=self._line_color,
            )
        if self._graph_type == GraphTypeOptions.BAR_CHART:
            trace = go.Bar(
                x=graph_data.x_data(),
                y=graph_data.y_data(),
                marker_color=self._line_color,
            )
        if not trace:
            raise ValueError(f'Graph type "{self._graph_type.value}" is not handled!')
        self._figure.add_trace(trace)

    def get_serialized_figure(self) -> dict:
        """Get figure on a JSON serialized format - i.e. a dictionary"""
        return self._figure.to_dict()
