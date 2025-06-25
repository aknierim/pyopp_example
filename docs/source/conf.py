#!/usr/bin/env python3
import datetime
import sys
from pathlib import Path

import pyopp

if sys.version_info < (3, 11):
    import tomli as tomllib
else:
    import tomllib

pyproject_path = Path(__file__).parent.parent.parent / "pyproject.toml"
pyproject = tomllib.loads(pyproject_path.read_text())
project = pyproject["project"]["name"]

author = pyproject["project"]["authors"][0]["name"]
copyright = "{}. Last updated {}".format(
    author, datetime.datetime.now().strftime("%d %b %Y %H:%M")
)

python_requires = pyproject["project"]["requires-python"]

# make some variables available to each page
rst_epilog = f"""
.. |python_requires| replace:: {python_requires}
"""


version = pyopp.__version__
# The full version, including alpha/beta/rc tags.
release = version


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.coverage",
    "sphinx.ext.viewcode",
    "sphinx_automodapi.automodapi",
    "sphinx_automodapi.smart_resolver",
    "numpydoc",
    "IPython.sphinxext.ipython_console_highlighting",
    "sphinx_copybutton",
    "nbsphinx",
]

numpydoc_show_class_members = False
numpydoc_class_members_toctree = False

intersphinx_mapping = {
    "numpy": ("https://numpy.org/doc/stable", None),
}

suppress_warnings = ["intersphinx.external"]

templates_path = ["_templates"]
exclude_patterns = ["build", "Thumbs.db", ".DS_Store", "changes", "*.log"]

source_suffix = ".rst"
master_doc = "index"


html_theme = "pydata_sphinx_theme"

html_static_path = ["source/_static"]
html_file_suffix = ".html"
html_css_files = ["custom.css"]

# html_favicon = "_static/favicon/favicon.ico"

html_theme_options = {
    "github_url": "https://github.com/aknierim/pyopp",
    "header_links_before_dropdown": 5,
    "navbar_start": ["navbar-logo"],
    "navigation_with_keys": False,
    "icon_links_label": "Quick Links",
    "announcement": """
        <p>pyopp is not stable yet, so expect large and rapid
        changes to structure and functionality as we explore various
        design choices before the 1.0 release.</p>
    """,
}

html_title = f"{project}"
htmlhelp_basename = project + "docs"
