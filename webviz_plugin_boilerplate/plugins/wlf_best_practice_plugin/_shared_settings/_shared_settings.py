from typing import List

import webviz_core_components as wcc
from dash.development.base_component import Component
from webviz_config.utils import StrEnum
from webviz_config.webviz_plugin_subclasses import SettingsGroupABC

from webviz_plugin_boilerplate._utils._data_model import DataNames

###################################################################
#
# Shared settings are settings shared across views in a plugin.
# This provides control/filtering of data sources to aggregate data
# to views and their respective view elements.
#
###################################################################


class DataNameSelection(SettingsGroupABC):
    class Ids(StrEnum):
        RADIO_ITEMS = "radio-items"

    def __init__(self) -> None:
        super().__init__("Data Selection")

    def layout(self) -> List[Component]:
        return [
            wcc.RadioItems(
                id=self.register_component_unique_id(DataNameSelection.Ids.RADIO_ITEMS),
                options=[
                    {
                        "label": "First data set",
                        "value": DataNames.FIRST.value,
                    },
                    {
                        "label": "Second data set",
                        "value": DataNames.SECOND.value,
                    },
                    {
                        "label": "Third data set",
                        "value": DataNames.THIRD.value,
                    },
                ],
                value=DataNames.FIRST.value,
            ),
        ]
