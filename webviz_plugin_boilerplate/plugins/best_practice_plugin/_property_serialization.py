from enum import Enum

import plotly.graph_objs as go

from ._business_logic import GraphData


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


class GraphTypeOptions(str, Enum):
    """
    Type definition of graph type options

    For de-serialization of graph mode selection in callback
    """

    LINE_PLOT = "Line plot"
    BAR_CHART = "Bar chart"


class GraphDataVisualizationOptions(str, Enum):
    """
    Type definition of graph data visualization options

    For de-serialization of graph data visualization selection in callback
    """

    RAW = "Raw"
    REVERSED = "Reversed"
    FLIPPED = "Flipped"


class GraphFigureBuilder:
    """
    Figure builder for creating/building output data for the callback

    Contains function for adding wanted data and function for getting
    the serialized data for callback Output
    """

    def __init__(self, graph_mode: GraphTypeOptions) -> None:
        self._figure = go.Figure()
        self._graph_mode = graph_mode

    def add_graph_title(self, title: str) -> None:
        self._figure.update_layout(title=title)

    def add_graph_data(self, graph_data: GraphData) -> None:
        trace = None
        if self._graph_mode == GraphTypeOptions.LINE_PLOT:
            trace = go.Scatter(x=graph_data.x(), y=graph_data.y(), mode="lines")
        if self._graph_mode == GraphTypeOptions.BAR_CHART:
            trace = go.Bar(x=graph_data.x(), y=graph_data.y())
        if not trace:
            raise ValueError(f'Graph mode "{self._graph_mode.value}" is not handled!')
        self._figure.add_trace(trace)

    def get_serialized_figure(self) -> dict:
        """Get figure on a JSON serialized format - i.e. a dictionary"""
        return self._figure.to_dict()
