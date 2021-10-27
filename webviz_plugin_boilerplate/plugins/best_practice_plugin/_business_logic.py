from typing import Dict, ItemsView, List


######################################################################
#
# Business logic is intended to possess data handling functionality
# separated from GUI code, i.e.separated from Dash-related code
# and visualization format (e.g. plotly when graphing data)
#
# Rule: No dash* import allowed
#
# Query database/input for relevant data and necessary ad-hoc
# calculations for data.
#
######################################################################


class GraphData:
    """Definition of graph data"""

    def __init__(self, x: List[int], y: List[int]) -> None:
        if len(x) != len(y):
            raise ValueError("Length of x and y data must be equal!")

        self._x = x
        self._y = y

    def x(self) -> List[int]:
        return self._x

    def y(self) -> List[int]:
        return self._y


class GraphSet:
    """
    Definition of graph set - set of graph data with unique names
    """

    def __init__(
        self,
        graph_dict: Dict[str, GraphData],
    ) -> None:
        self._graph_dict = graph_dict.copy()

    def items(self) -> ItemsView[str, GraphData]:
        return self._graph_dict.items()

    def graph_names(self) -> List[str]:
        return list(self._graph_dict.keys())

    def graph_data(self, graph_name: str) -> GraphData:
        if graph_name not in self.graph_names():
            raise ValueError(
                f'Graph with name "{graph_name}" not present in graph set!'
            )
        return self._graph_dict[graph_name]


class GraphDataModel:
    def __init__(self) -> None:
        self._graph_set: GraphSet

    def populate_with_mock_data(self):
        graph_dict: Dict[str, GraphData] = {
            "First Graph": GraphData(x=[0, 1, 2, 3, 4], y=[1, 3, -2, 5, 0]),
            "Second Graph": GraphData(x=[0, 1, 2, 3, 4], y=[-3, 4, 0, 2, 6]),
            "Third Graph": GraphData(x=[0, 1, 2, 3, 4], y=[0, 2, 4, 2, 0]),
        }
        self._graph_set = GraphSet(graph_dict)

    def graph_set(self) -> GraphSet:
        return self._graph_set

    @staticmethod
    def create_reversed_data(graph_data: GraphData) -> GraphData:
        x = graph_data.x().copy()
        y = graph_data.y().copy()
        list.reverse(y)
        return GraphData(x, y)

    @staticmethod
    def create_flipped_data(graph_data: GraphData) -> GraphData:
        x = graph_data.x().copy()
        y = [-elm for elm in graph_data.y()]
        return GraphData(x, y)
