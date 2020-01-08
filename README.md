[![Build Status](https://travis-ci.org/equinor/webviz-plugin-boilerplate.svg?branch=master)](https://travis-ci.org/equinor/webviz-plugin-boilerplate)
[![Python 3.6 | 3.7](https://img.shields.io/badge/python-3.6%20|%203.7-blue.svg)](https://www.python.org/)

# Quickly get started creating plugins to `webviz-config`

This repository will quickly get you started creating your own [`webviz-config`](https://github.com/equinor/webviz-config) plugins :rocket:.

<br/>

## Create a new Python plugin package

Creating a new Python package with [`webviz-config`](https://github.com/equinor/webviz-config) plugins is one or two commands only.

1. :cookie: **Install `cookiecutter`.** If [`cookiecutter`](https://github.com/cookiecutter/cookiecutter) is not already installed, we will have to do that first. One approach is to create a new [virtual environment](https://docs.python.org/3/tutorial/venv.html) and then install it using `pip`:

   ```bash
   python -m venv ./my_new_venv
   source ./my_new_venv/bin/activate
   pip install cookiecutter
   ```
   
2. :running: **Run `cookiecutter`.**
   ```bash
   cookiecutter gh:equinor/webviz-plugin-boilerplate
   ```

3. :question: **Fill in the questions asked.** Project name, author name etc.

4. :bouquet: **Done!** You will now have a new Python package folder (with your project name) generated for you.
<br/>

## Install your new Python plugin package

The default package created for you contains some dummy plugins. These you can later delete/and or overwrite with your fancy plugins. You can have an arbitrary number of plugins in your package.

To install your plugin package in _development mode_, run
```bash
cd YOUR_PLUGIN_PROJECT
pip install -e .
```
This will (first time) install all dependencies, but the `-e` flag will also make sure your plugin project is installed in edit/development mode. This means that when you update the Python files in your package, this will automatically be available in your current Python environment without having to reinstall the package.

> :beetle: If installation of your package fails with `LookupError: setuptools-scm was unable to detect version`, this is because your package is not in a git repository (it tries to use git repository tag as version). We recommend putting your plugin package under version control as e.g. a [GitHub repository](http://github.com). This will, in addition to version control, make it easy for others to collaborate on the project, automatic security scan of your dependencies, and other useful stuff.
> 
> If you for now just want to get the installation done, and wait with creating a repository, you can explicitly set a version (before running `pip install -e .`) using the following command:
> ```
> export SETUPTOOLS_SCM_PRETEND_VERSION=0.1.0
> ```
<br/>

## Test your new Python plugin package

After installation you can test the custom plugins from your package using the provided example configuration file:
```bash
webviz build ./examples/basic_example.yaml
```
<br/>

## Make awesome stuff :eyeglasses:

You are now ready to modify the package with your own plugins. Have fun! :cake:
