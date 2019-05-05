# -*- coding: utf-8; mode: python -*-
"""built in fonts"""

import mimetypes
import fspath
# https://tinycss.readthedocs.io/en/latest/
import tinycss
from tinycss.fonts3 import FontFaceRule

FILES = dict()
BASE  = fspath.FSPath(__file__).DIRNAME

# for folder in [BASE/'dejavu', BASE/'cantarell']:
#     for f in folder.glob('*.*'):
#         mtype, encoding = mimetypes.guess_type(f)
#         if mtype and mtype.startswith('font/'):
#             FILES[f] = mtype, encoding

for name in [ 'cantarell', 'dejavu']:

    css_file = BASE / name / name + ".css"
    parser = tinycss.make_parser('fonts3')
    stylesheet = parser.parse_stylesheet_file(css_file)

    # filter @font-face rules
    font_face_rules = [ rule for rule in stylesheet.rules
                        if isinstance(rule, FontFaceRule) ]

    for rule in font_face_rules:
        l_font_family = []
        l_uri = []

        for decl in rule.declarations:
            if decl.name == 'font-family':
                for token in decl.value:
                    font_family.append(token.value)

            if decl.name == 'src':
                for token in decl.value:
                    if token.type == 'URI':
                        uri.append(BASE/name/token.value)

        # TODO: die fonts und urls müssen jetzt noch verarbeitet werden ..
        # Es kann ja auch http: URLs (font CDN geben), die sollte man auch verarbeiten
        # um ggf. Fonts aus dem netz zu laden.
