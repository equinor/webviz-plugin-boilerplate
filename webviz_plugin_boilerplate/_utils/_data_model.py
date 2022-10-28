from enum import Enum
from typing import Dict, ItemsView, List

######################################################################
#
# Data mode is intended to possess data handling functionality
# separated from GUI code, i.e.separated from Dash-related code
# and visualization format (e.g. plotly when graphing data)
#
# Rule: No dash* import allowed
#
# Query database/input for relevant data and necessary ad-hoc
# calculations for data.
#
######################################################################


class DataNames(str, Enum):
    FIRST = "first"
    SECOND = "second"
    THIRD = "third"


class Data:
    """Definition of sample data"""

    def __init__(self, x_data: List[int], y_data: List[int]) -> None:
        if len(x_data) != len(y_data):
            raise ValueError("Length of x and y data must be equal!")

        self._x_data = x_data
        self._y_data = y_data

    def x_data(self) -> List[int]:
        return self._x_data

    def y_data(self) -> List[int]:
        return self._y_data

    def num_samples(self) -> int:
        return len(self._x_data)


class DataSet:
    """
    Definition of data set - set of sample data with unique names
    """

    def __init__(
        self,
        data_sample_dict: Dict[DataNames, Data],
    ) -> None:
        self._data_sample_dict = data_sample_dict.copy()

    def items(self) -> ItemsView[DataNames, Data]:
        return self._data_sample_dict.items()

    def names(self) -> List[str]:
        return [elm.value for elm in self._data_sample_dict.keys()]

    def get_data(self, name: DataNames) -> Data:
        if name not in self._data_sample_dict.keys():
            raise ValueError(f'Data with name "{name.value}" not present in data set!')
        return self._data_sample_dict[name]


class DataModel:
    def __init__(self) -> None:
        self._data_set: DataSet

    def populate_with_mock_data(self):
        _x = list(range(0, 10))
        data_sample_dict: Dict[DataNames, Data] = {
            DataNames.FIRST: Data(x_data=_x, y_data=[x * x for x in _x]),
            DataNames.SECOND: Data(x_data=_x, y_data=[1, 3, -2, 5, 0, 7, 3, -5, -1, 3]),
            DataNames.THIRD: Data(x_data=_x, y_data=[0, 2, 4, 6, 8, 4, 2, 0, -2, -4]),
        }
        self._data_set = DataSet(data_sample_dict)

    def data_set(self) -> DataSet:
        return self._data_set
