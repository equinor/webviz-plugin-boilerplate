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
   cookiecutter gh:equinor/webviz-container-boilerplate
   ```

3. :question: **Fill in the questions asked.** Project name, author name etc.

4. :bouquet: **Done!** You will now have a new Python package folder (with your project name) generated for you.
<br/>

## Install your new Python plugin package

The default package created for you contains some dummy containers. These you can later delete/and or overwrite with your fancy containers. You can have an arbitrary number of containers in your package.

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

After installation you can test the custom containers from your package using the provided example configuration file:
```bash
webviz build ./examples/basic_example.yaml
```
<br/>

## Make awesome stuff :eyeglasses:

You are now ready to modify the package with your own containers. Have fun! :cake:
