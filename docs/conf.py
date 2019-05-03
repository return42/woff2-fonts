# -*- coding: utf-8 -*-
#
# Sphinx documentation build configuration file

import re
import pyfonts
import sphinx_rtd_theme

master_doc = 'index'
templates_path = ['_templates']
exclude_patterns = ['_build', 'slides']

project   = 'pyfonts'
copyright = pyfonts.__copyright__
version   = pyfonts.__version__
release   = pyfonts.__version__
show_authors = True

extensions = [
    'sphinx.ext.autodoc'
    , 'sphinx.ext.extlinks'
    #, 'sphinx.ext.autosummary'
    #, 'sphinx.ext.doctest'
    , 'sphinx.ext.todo'
    , 'sphinx.ext.coverage'
    #, 'sphinx.ext.pngmath'
    #, 'sphinx.ext.mathjax'
    , 'sphinx.ext.viewcode'
    , 'sphinx.ext.intersphinx'
]

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ["../utils/sphinx-static"]
html_context = {
    'css_files': [
        '_static/theme_overrides.css',
    ],
}
html_logo = 'darmarIT_logo_128.png'

# disable tls_verify for intersphinx url's with self signed certifacates
# tls_verify = False
intersphinx_mapping = {}
