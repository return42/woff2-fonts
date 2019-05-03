.. -*- coding: utf-8; mode: rst -*-

===========
WOFF2 fonts
===========

WOFF2 W3C Recommendation
  - https://www.w3.org/TR/WOFF2/

OFL fonts:
  - `SIL OFL<https://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&item_id=OFL>`_
  - https://fontlibrary.org/en/search?license=OFL%20(SIL%20Open%20Font%20License)

Variable Fonts (VF):
  - https://css-tricks.com/one-file-many-options-using-variable-fonts-web
  - https://v-fonts.com/

fonttools:
  Tool for manipulating TrueType and OpenType fonts

  - `fonttools <https://github.com/fonttools/fonttools>`_

  Install method using python3 & install fonttools and brotli compression::

    $ sudo apt-get install python3-dev
    $ pip3 install --user fonttools
    $ git clone https://github.com/google/brotli
    cd brotli
    $ python3 setup.py install --user

Cantarell
=========

WOFF2 format of Cantarell Variable Font TTF (origin)

font
  Cantarell-VT (Variable Font) v0.111 (commit 8cf8f934)

CSS
  `./cantarell/cantarell.css`_

  - Cantarell

origin
  https://gitlab.gnome.org/GNOME/cantarell-fonts

license
  ./cantarell/COPYING

build
  WOFF2 format was generated from the ttf files using ``pyftsubset`` command
  from the fonttools_ lib::

    $ pyftsubset Cantarell-VF.ttf --output-file="Cantarell-VF.woff2"


DejaVu
======

WOFF2 format of DejaVu TTF (origin)

font
  DejaVu v2.37

CSS
  `./dejavu/dejavu.css`_

  - DejaVu Sans
  - DejaVu Sans Bold
  - DejaVu Sans Bold Oblique
  - DejaVu Sans Condensed
  - DejaVu Sans Condensed Bold
  - DejaVu Sans Condensed Bold Oblique
  - DejaVu Sans Condensed Oblique
  - DejaVu Sans ExtraLight
  - DejaVu Sans Mono
  - DejaVu Sans Mono Bold
  - DejaVu Sans Mono Bold Oblique
  - DejaVu Sans Mono Oblique
  - DejaVu Sans Oblique
  - DejaVu Serif
  - DejaVu Serif Bold
  - DejaVu Serif Bold Italic
  - DejaVu Serif Condensed
  - DejaVu Serif Condensed Bold
  - DejaVu Serif Condensed Bold Italic
  - DejaVu Serif Condensed Italic
  - DejaVu Serif Italic
  - DejaVu Math TeX Gyre

origin
  https://github.com/dejavu-fonts/dejavu-fonts/releases/download/version_2_37/dejavu-fonts-ttf-2.37.tar.bz2

license
  `./dejavu/LICENSE.html`_

build
  WOFF2 format was generated from the ttf files using ``pyftsubset`` command
  from the fonttools_ lib::

    # switch into fonts folder and convert ttf to WOFF2
    $ cd dejavu-fonts-ttf-2.37/ttf/
    $ mkdir ../woff2
    $ for ttf in *.ttf; do \
        pyftsubset $ttf --output-file="../woff2/${ttf%.*}.woff2" \
        --unicodes=U+0-10FFFF --layout-features='*' --flavor=woff2; \
      done
    WARNING: FFTM NOT subset; don't know how to subset; dropped
    # ignore warnings about the FontForge time stamp table (FFTM)

