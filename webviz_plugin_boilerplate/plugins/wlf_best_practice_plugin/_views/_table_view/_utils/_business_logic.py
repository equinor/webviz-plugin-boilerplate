from webviz_plugin_boilerplate._utils._data_model import Data

from .._settings import TableOrder

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


def create_table_data_with_order(data: Data, order: TableOrder) -> Data:
    """
    Business logic for handling order of data samples.

    The extraction is only to illustrate separation/structuring of business code
    """
    _x = data.x_data().copy()
    _y = data.y_data().copy()

    if order is TableOrder.DESC:
        _x.reverse()
        _y.reverse()

    return Data(_x, _y)
