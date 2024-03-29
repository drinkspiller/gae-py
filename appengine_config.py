"""
`appengine_config.py` is automatically loaded when Google App Engine
starts a new instance of your application. This runs before any
WSGI applications specified in app.yaml are loaded.

Run 'pip install package_name -t lib/' to install these dependencies
in `lib/` subdirectory.
"""

from google.appengine.ext import vendor

# Third-party libraries are stored in "lib", vendoring will make
# sure that they are importable by the application.
vendor.add('lib')
