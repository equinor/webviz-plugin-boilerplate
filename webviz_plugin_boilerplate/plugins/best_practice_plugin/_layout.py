from typing import Callable, List

import webviz_core_components as wcc

from ._property_serialization import GraphDataVisualizationOptions, GraphTypeOptions

######################################################################
#
# Collection of Dash layout and ID-ownership
#
# Defines the Dash layout, and builds the HTML-element structure
# for the plugin.
#
# Ownership of the layout element ID's, which is provied to the
# various callback Inputs, States and Outputs.
#
######################################################################

# pylint: disable = too-few-public-methods
class LayoutElements:
    """
    Definition of names/ID's of HTML-elements in view

    Layout file is owner of ID's and provides the definition to the users,
    e.g. callbacks (Input, State and Output properties).

    NOTE: Other solutions can be used, the main goal is to have a set of defined
    names for element ID which is provided to callbacks - preventing hard coded
    string values.
    """

    GRAPH = "graph"

    GRAPH_SELECTION_DROPDOWN = "graph_selection_dropdown"
    GRAPH_TYPE_RADIO_ITEMS = "graph_type_radio_items"
    GRAPH_DATA_VISUALIZATION_RADIO_ITEMS = "graph_data_visualization_radio_items"


def main_layout(get_uuid: Callable, graph_names: List[str]) -> wcc.FlexBox:
    return wcc.FlexBox(
        children=[
            wcc.FlexColumn(
                children=wcc.Frame(
                    style={"height": "90vh"},
                    children=[
                        wcc.Selectors(
                            label="Graphs",
                            children=[
                                wcc.Dropdown(
                                    label="Selected graph",
                                    id=get_uuid(
                                        LayoutElements.GRAPH_SELECTION_DROPDOWN
                                    ),
                                    options=[
                                        {"label": name, "value": name}
                                        for name in graph_names
                                    ],
                                    value=graph_names[0],
                                )
                            ],
                        ),
                        wcc.Selectors(
                            label="Graph type",
                            children=[
                                wcc.RadioItems(
                                    id=get_uuid(LayoutElements.GRAPH_TYPE_RADIO_ITEMS),
                                    options=[
                                        {
                                            "label": GraphTypeOptions.LINE_PLOT.value,
                                            "value": GraphTypeOptions.LINE_PLOT.value,
                                        },
                                        {
                                            "label": GraphTypeOptions.BAR_CHART.value,
                                            "value": GraphTypeOptions.BAR_CHART.value,
                                        },
                                    ],
                                    value=GraphTypeOptions.LINE_PLOT.value,
                                )
                            ],
                        ),
                        wcc.Selectors(
                            label="Graph data vitalization",
                            children=[
                                wcc.RadioItems(
                                    id=get_uuid(
                                        LayoutElements.GRAPH_DATA_VISUALIZATION_RADIO_ITEMS
                                    ),
                                    options=[
                                        {
                                            "label": "Raw data",
                                            "value": GraphDataVisualizationOptions.RAW.value,
                                        },
                                        {
                                            "label": "Reversed data",
                                            "value": GraphDataVisualizationOptions.REVERSED.value,
                                        },
                                        {
                                            "label": "Flipped data",
                                            "value": GraphDataVisualizationOptions.FLIPPED.value,
                                        },
                                    ],
                                    value=GraphDataVisualizationOptions.RAW.value,
                                ),
                            ],
                        ),
                    ],
                )
            ),
            wcc.FlexColumn(
                flex=4,
                children=[
                    wcc.Frame(
                        style={"height": "90vh"},
                        highlight=False,
                        color="white",
                        children=wcc.Graph(
                            style={"height": "85vh"},
                            id=get_uuid(LayoutElements.GRAPH),
                        ),
                    )
                ],
            ),
        ],
    )
