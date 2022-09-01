## This is an exampled of plugin structure for plugins written by use of the `Webviz Layout Framework` - `WLF`

<br/>
The example below shows the best practice folder and file structure while using `WLF` for plugin implementation. 
<br/><br/>

## Example file/folder structure with `WLF`

```python
plugins/
└── _my-plugin
    ├── (_callbacks) # if the callback code in your plugin file exceeds 100(?) lines of code
    │   ├── ...
    │   └── __init__.py
    ├── __init__.py
    ├── _plugin_ids.py
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
