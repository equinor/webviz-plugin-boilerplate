## File structure for `Webviz Layout Framework` - `WLF`

The examples below shows the best practice folder and file structure while using `WLF` for plugin implementation. This is a guideline of how a plugin can be structured with files and folders to keep an overview and control of the views and their content - both settings, view elements, business logic and utility functionality.
<br/><br/>
The most important aspect of the `WLF` is the class/object dependence - i.e. which `WLF` classes are dependent of each other. The hierarchy is a plugin (`WebvizPluginABC`) which contains views (`ViewABC`). The views can contain settings (`SettingsGroupABC`) and view elements (`ViewElementABC`). These settings should then affect the data visualized across all view elements in the view. There is also possible to have settings (`SettingsGroupABC`) within a specific view element, if the settings only affects the specific view element. With a graph object as a view element such settings can be e.g. line colors, axis names, toggle on/off legends etc.
<br/><br/>
It is up to the plugin author to find a clear structure of the files for easier readability and maintainability. If the various content of view objects contains few lines of codes, the views, settings, view elements and their content can be placed within a single file if wanted. The only criteria is that the plugins contain a file `_plugin.py` and a folder `_views` for the plugin views.
<br/><br/>

---

## Minimum criteria of file/folder structure with `WLF`

This shows the minimum file/folder structure for a plugin written by use of `WLF`. Even with a single view, the `_view1` should be placed within a `_views` folder. This makes it easier to reuse the view and add a new view to the plugin at a later point.
<br/><br/>

```python
plugins/
└── _my-plugin
    ├── __init__.py
    ├── _plugin.py
    └── _views
        ├── __init__.py
        ├── _view1
        │   ├── __init__.py
        │   ├── (_utils) # only if the view has its own utility functions
        │   │   ├── ...
        │   │   └── __init__.py
        │   └── _view.py
        └── _view2
            ├── __init__.py
            ├── (_utils) # only if the view has its own utility functions
            │   ├── ...
            │   └── __init__.py
            └── _view.py

```

---

## Example file/folder structure with `WLF`

This is an exampled of file/folder structure for a large plugin written by use of `WLF`. This is a guide line of how to structure content when object implementations becomes large, and the need of separation into multiple files are necessary. The content of the views placed in the `_views` folder increases, and needs to be separated into multiple files placed within subfolder. When implementation of settings and view elements becomes large, they can be separated into multiple files and placed within the `_settings` and `_view_elements` folders. The view elements settings are placed inside the subfolder for the respective view element - e.g. `_view_element1/_settings`.
<br/><br/>

```python
plugins/
└── _my-plugin
    ├── (_callbacks) # if the callback code in your plugin file exceeds 100(?) lines of code
    │   ├── ...
    │   └── __init__.py
    ├── __init__.py
    ├── _plugin.py
    ├── (_shared_settings) # only required if you have settings which are shared by multiple views
    │   └── __init__.py
    ├── (_shared_view_elements) # only if you have view elements which are used in multiple views - e.g. a view element containing a single graph - NOTE: this makes the views harder to reuse
    ├── (_utils) # only if you have any utility functions which are either used by multiple views/view elements/settings and/or in the plugin itself - if they are only used in a view group or a single view, place them in the respective view (group) folder
    │   ├── ...
    │   └── __init__.py
    └── _views
        ├── __init__.py
        ├── _view1
        │   ├── __init__.py
        │   ├── (_settings) # only if the view has its own settings (i.e. settings which are not shared)
        │   │   ├── ...
        │   │   └── __init__.py
        │   ├── (_utils) # only if the view has its own utility functions
        │   │   ├── ...
        │   │   └── __init__.py
        │   ├── (_view_elements) # only if the view has its own view elements which are not shared with other views
        │   │   ├── __init__.py
        │   │   └── _view_element1
        │   │       ├── __init__.py
        │   │       ├── (_settings) # only if the view element has its own settings
        │   │       │   ├── ...
        │   │       │   └── __init__.py
        │   │       └── _view_element.py
        │   └── _view.py
        └── _view_group1 # only if you have a view group with multiple views
            ├── __init__.py
            ├── (_utils) # utility functions shared by several views in this view group
            │   ├── ...
            │   └── __init__.py
            ├── (_shared_view_elements) # only if you have view elements which are used in more than one sub view - e.g. a view element containing a single graph
            │   ├── ...
            │   └── __init__.py
            ├── _view1
            │   ├── __init__.py
            │   ├── (_settings) # only if the view has its own settings (i.e. settings which are not shared)
            │   │   ├── ...
            │   │   └── __init__.py
            │   ├── (_utils) # only if the view has its own utility functions
            │   │   ├── ...
            │   │   └── __init__.py
            │   ├── (_view_elements) # only if the view has its own view elements which are not shared with
            │   │   ├── __init__.py
            │   │   └── _view_element1
            │   │       ├── __init__.py
            │   │       ├── (_settings) # only if the view element has its own settings
            │   │       │   ├── ...
            │   │       │   └── __init__.py
            │   │       └── _view_element.py
            │   └── _view.py
            └── _view2
                ├── __init__.py
                ├── (_settings) # only if the view has its own settings (i.e. settings which are not shared)
                │   ├── ...
                │   └── __init__.py
                ├── (_utils) # only if the view has its own utility functions
                │   ├── ...
                │   └── __init__.py
                ├── (_view_elements) # only if the view has its own view elements which are not shared with
                │   ├── __init__.py
                │   └── _view_element1
                │       ├── __init__.py
                │       ├── (_settings) # only if the view element has its own settings
                │       │   ├── ...
                │       │   └── __init__.py
                │       └── _view_element.py
                └── _view.py

```
