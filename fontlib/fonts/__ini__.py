# -*- coding: utf-8; mode: python -*-
"""built in fonts"""

import mimetypes
import fspath

# https://tinycss.readthedocs.io/en/latest/
import tinycss

BASE  = fspath.FSPath(__file__).DIRNAME
FILES = dict()

# for folder in [BASE/'dejavu', BASE/'cantarell']:
#     for f in folder.glob('*.*'):
#         mtype, encoding = mimetypes.guess_type(f)
#         if mtype and mtype.startswith('font/'):
#             FILES[f] = mtype, encoding

for name in ['dejavu', 'cantarell']:
    css_file = BASE / name / name + ".css"
    parser = tinycss.make_parser('fonts3')
    stylesheet = parser.parse_stylesheet_file(css_file)

    print(stylesheet.rules)
    
