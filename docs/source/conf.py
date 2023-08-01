# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
# -- Path setup ----------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

########### TRICK FOUND ON SOME TUTORIAL : ADD IN THE MOCK_MODULES ANY EXTERNAL MODULE YOU'RE USING IN YOUR PACKAGE.

import mock

MOCK_MODULES = ['numpy']
for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = mock.Mock()

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Py-Doc'
copyright = '2023, Connor Holm'
author = 'Connor Holm'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'recommonmark',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode'
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
