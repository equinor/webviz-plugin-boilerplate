from enum import Enum
from typing import Type

from dash import dash_table, html
from dash.development.base_component import Component
from webviz_config.webviz_plugin_subclasses import ViewElementABC


class TableViewElement(ViewElementABC):
    """View element for table

    The view element contains a table object for showing
    data.

    `View element content:`
    - Label for title
    - Table object
    """

    class Ids(str, Enum):
        TABLE = "table"
        TITLE = "title"

    def __init__(self, height: str = "86vh") -> None:
        super().__init__()
        self._height = height

    def inner_layout(self) -> Type[Component]:
        return html.Div(
            children=[
                html.Label(
                    id=self.register_component_unique_id(
                        TableViewElement.Ids.TITLE.value
                    ),
                ),
                dash_table.DataTable(
                    id=self.register_component_unique_id(
                        TableViewElement.Ids.TABLE.value
                    ),
                    columns=[{"id": "x", "name": "X"}, {"id": "y", "name": "Y"}],
                ),
            ]
        )
