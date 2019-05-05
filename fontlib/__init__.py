# -*- coding: utf-8; mode: python -*-

import mimetypes
import pkg_resources
import fspath
from . import __pkginfo__

pkg_resources.declare_namespace(__name__)

__version__   = __pkginfo__.version
__author__    = __pkginfo__.authors[0]
__license__   = __pkginfo__.license
__copyright__ = __pkginfo__.copyright
__doc__       = __pkginfo__.docstring

PKG_FOLDER = fspath.FSPath(__file__).DIRNAME
FONT_FILES = dict()

def _init():

    # register mimetypes
    mtypes = mimetypes.read_mime_types(PKG_FOLDER / 'mime.types')
    for ext, mtype in mtypes.items():
        mimetypes.add_type(mtype, ext)

    # register font files
    for ep  in ['fonts_ttf', 'fonts_otf']:
        for entry_point in pkg_resources.iter_entry_points(ep):
            FONT_FILES.update(entry_point.load())



        
for entry_point in pkg_resources.iter_entry_points('fonts_otf'):
    font_files.update(entry_point.load())

for font in font_files:
    globals()[font] = font_files[font]





# def on_build_finished(app, exc):
#     # type: (Sphinx, Exception) -> None
#     if exc is None:
#         src = path.join(sphinx.package_dir, 'templates', 'graphviz', 'graphviz.css')
#         dst = path.join(app.outdir, '_static')
#         copy_asset(src, dst)


# def setup(app):
#     # type: (Sphinx) -> Dict[str, Any]
#     app.add_node(graphviz,
#                  html=(html_visit_graphviz, None),
#                  latex=(latex_visit_graphviz, None),
#                  texinfo=(texinfo_visit_graphviz, None),
#                  text=(text_visit_graphviz, None),
#                  man=(man_visit_graphviz, None))
#     app.add_directive('graphviz', Graphviz)
#     app.add_directive('graph', GraphvizSimple)
#     app.add_directive('digraph', GraphvizSimple)
#     app.add_config_value('graphviz_dot', 'dot', 'html')
#     app.add_config_value('graphviz_dot_args', [], 'html')
#     app.add_config_value('graphviz_output_format', 'png', 'html')
#     app.add_css_file('graphviz.css')
#     app.connect('build-finished', on_build_finished)
#     return {'version': sphinx.__display_version__, 'parallel_read_safe': True}
