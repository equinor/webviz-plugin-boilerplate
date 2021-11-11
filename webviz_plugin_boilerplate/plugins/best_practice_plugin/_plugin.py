from typing import Union, Type

from webviz_config import WebvizPluginABC

from dash import Dash
from dash.development.base_component import Component

from ._business_logic import GraphDataModel
from ._callbacks import plugin_callbacks
from ._layout import main_layout


class BestPracticePlugin(WebvizPluginABC):
    """
    This Webviz plugin, to illustrate a best practice on code structure and how to
    separate code for clarity and usability.

    The plugin subclasses the abstract WebvizPluginABC base class, and implements
    the required layout function, in addition to callback functionality.

    `Plugin functionality`:
    Plugin contains a model for graph data, which is populated with a set of mocked up
    graph data with unique names. The plugin provides a dropdown for selecting a
    specific graph name from the set and show the graph data in plot. The model provides
    additional ad-hoc calculations (raw, reversed and flipped) for the selected graph
    data. Based on selected visualization option in the layout, the callback retrieves
    correct graph data from the model and provides it to the graph builder in the property
    serialization. Graph type options are provided (line plot and bar chart) as radio items
    for specifying which type of graphing should be used in the graph builder. When the
    graph is built, the builder can provide the JSON serialized result for the callback
    Output.

    `Plugin file structure:`
    * _layout.py - Dash layout and ID-ownership
    * _callbacks.py - Dash callbacks for handling user interaction and update of view
    * _business_logic.py - Query database/input for relevant data and necessary
    ad-hoc calculations for data, separated from Dash specific code (no dash* import)
    * _prop_serialization.py - De-serializing and serializing callback property formats.
    Convert callback Input/State from JSON serializable property formats to strongly typed
    formats (de-serialize) for business logic. Create/build JSON serializable properties
    for Dash callback Output property by use of data from business logic.
    """

    def __init__(self, app: Dash) -> None:
        super().__init__()

        self._graph_data_model = GraphDataModel()
        self._graph_data_model.populate_with_mock_data()

        self.set_callbacks(app)

    @property
    def layout(self) -> Union[str, Type[Component]]:
        return main_layout(
            get_uuid=self.uuid,
            graph_names=self._graph_data_model.graph_set().graph_names(),
        )

    def set_callbacks(self, app) -> None:
        plugin_callbacks(app, self.uuid, self._graph_data_model)
