import dash_html_components as html
from webviz_config import WebvizContainerABC


class SomeCustomContainer(WebvizContainerABC):
    @property
    def layout(self):
        return html.Div(
            [html.H1("This is a static title"), "And this is just some ordinary text"]
        )
