from webviz_plugin_boilerplate._utils._data_model import Data

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


def create_reversed_data(data: Data) -> Data:
    x_data = data.x_data().copy()
    y_data = data.y_data().copy()
    list.reverse(y_data)
    return Data(x_data, y_data)


def create_flipped_data(data: Data) -> Data:
    x_data = data.x_data().copy()
    y_data = [-elm for elm in data.y_data()]
    return Data(x_data, y_data)
