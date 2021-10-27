[![Build Status](https://github.com/equinor/webviz-plugin-boilerplate/workflows/webviz-plugin-boilerplate/badge.svg)](https://github.com/equinor/webviz-plugin-boilerplate/actions?query=branch%3Amaster)
[![Python 3.6 | 3.7 | 3.8](https://img.shields.io/badge/python-3.6%20|%203.7%20|%203.8%20|%203.9-blue.svg)](https://www.python.org/)

# Quickly get started creating plugins to `webviz-config`

This repository will quickly get you started creating your own [`webviz-config`](https://github.com/equinor/webviz-config) plugins :rocket:.

<br/>

## Create a new Python plugin package

Creating a new Python package with [`webviz-config`](https://github.com/equinor/webviz-config) plugins by pushing [`Use this template`](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)-button.

Configure new python package in repository by the following steps

1. Rename project
2. Rename/Delete existing example plugins

## Install your new Python plugin package

The default package created for you contains some dummy plugins. These you can later delete/and or overwrite with your fancy plugins. You can have an arbitrary number of plugins in your package.

To install your plugin package in _development mode_, run

```bash
cd YOUR_PLUGIN_PROJECT
pip install -e .
```

This will (first time) install all dependencies, but the `-e` flag will also make sure your plugin project is installed in edit/development mode. This means that when you update the Python files in your package, this will automatically be available in your current Python environment without having to reinstall the package.

## Test your new Python plugin package

After installation you can test the custom plugins from your package using the provided example configuration file:

```bash
webviz build ./examples/boilerplate_example.yaml
```

<br/>

If you want to install test and linting dependencies, you can in addition run

```bash
pip install .[tests]
```

### Linting

You can do automatic linting of your code changes by running

```bash
black --check webviz_plugin_boilerplate # Check code style
pylint webviz_plugin_boilerplate # Check code quality
bandit -r webviz_plugin_boilerplate  # Check Python security best practice
```

### Usage and documentation

For general usage, see the documentation on
[webviz-config](https://github.com/equinor/webviz-config).

## Make awesome stuff :eyeglasses:

You are now ready to modify the package with your own plugins. Have fun! :cake:
