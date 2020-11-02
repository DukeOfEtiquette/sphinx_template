# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('./_ext'))

import sphinx_veldus_theme
import veldus_ext

extensions = [
  # 'veldus_ext.helloworld',
  'veldus_ext.todo',
  'veldus_ext.statblock',
  'sphinx_veldus_theme',
]

todo_include_todos = True

# -- Project information -----------------------------------------------------

project = 'Sphinx Template'
copyright = '2020, Adam DuQuette <duquetteadam@gmail.com>'
author = 'Adam DuQuette <duquetteadam@gmail.com>'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
  'dm_zone'
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_veldus_theme'

html_theme_options = {
  'collapse_navigation': False,
  'sticky_navigation': False,
  'style_external_links': True,
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_favicon = '_static/favicon.svg'

html_css_files = [
    'css/custom.css',
]

html_js_files = [
    'js/custom.js',
]

html_show_sourcelink = False

html_context = {
  'display_github': False,
  'github_user': 'DukeOfEtiquette',
  'github_repo': 'veldus_sphinx',
  'github_version': 'master/source/'
}
