from typing import List

from webviz_plugin_boilerplate._utils._data_model import Data

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
# Dash a layout element could be e.g. a table figure. The
# serialization retrieves data for table, and builds a table
# figure. The figure can be obtained in the callback functionality
# and be provided as a serialized property format for the data view
# object in the callback Output list.
#
# Dash callback for properties must be JSON serializable.
# In general, Dash properties can only be dash components, strings,
# dictionaries, numbers, None, or lists of those.
#
###################################################################


class TableDataBuilder:
    """
    Figure builder for creating/building serializable Output property data
    for the callback.

    Contains functions for adding table data and retrieving the serialized
    data for callback Output property.
    """

    def __init__(self) -> None:
        self._table_data: List[dict] = []

    def add_table_data(self, table_data: Data) -> List[dict]:
        _x = table_data.x_data().copy()
        _y = table_data.y_data().copy()

        self._table_data.extend(
            [{"x": _x[i], "y": _y[i]} for i in range(0, table_data.num_samples())]
        )

    def get_serialized_table_data(self) -> List[dict]:
        return self._table_data
