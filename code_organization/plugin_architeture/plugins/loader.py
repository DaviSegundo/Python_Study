"""
A simple plugin loader.
"""

import importlib
from typing import List


class PluginInterface:
    """A plugin has a single function called initialize."""

    @staticmethod
    def initialize() -> None:
        """Initialize the plugin."""


def import_module(name: str) -> PluginInterface:
    return importlib.import_module(name)

def load_plugins(plugins: List[str]) -> None:
    """Load the plugins defined in the plugins list.

    Args:
        plugins (List[str]): list thats contain the plugins.
    """
    for plugin_name in plugins:
        plugin = import_module(plugin_name)
        plugin.initialize()
