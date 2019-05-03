# -*- coding: utf-8; mode: python -*-
# pylint: disable=invalid-name,redefined-builtin
"""
python package meta informations
"""

package      = 'pyfonts'
version      = '20190503'
authors      = ['Markus Heiser', ]
emails       = ['markus.heiser@darmarIT.de', ]
copyright    = '2019 Markus Heiser'
url          = 'https://github.com/return42/pyfonts'
description  = 'Sphinx-doc extensions to embed WOFF2 fonts in HTML outputs'
license      = 'GPLv2'
keywords     = 'sphinx extension WOFF2'
docs         = 'http://return42.github.io/pyfonts'
repository   = 'https://github.com/return42/pyfonts'

install_requires = [ ]

def get_entry_points():
    """get entry points of the python package"""
    return {}

# See https://pypi.python.org/pypi?%3Aaction=list_classifiers
classifiers = [
    "Development Status :: 5 - Production/Stable"
    , "Intended Audience :: Developers"
    , "License :: OSI Approved :: GNU General Public License v2 (GPLv2)"
    , "Operating System :: OS Independent"
    , "Programming Language :: Python"
    , "Programming Language :: Python :: 3"
]
