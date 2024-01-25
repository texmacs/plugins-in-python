#!/usr/bin/env python
###############################################################################
##
## MODULE      : tikz.py
## DESCRIPTION : TikZ support
## COPYRIGHT   : (C) 2019  Darcy Shen, Massimiliano Gubinelli
##
## This software falls under the GNU general public license version 3 or later.
## It comes WITHOUT ANY WARRANTY WHATSOEVER. For details, see the file LICENSE
## in the root directory or <http://www.gnu.org/licenses/gpl-3.0.html>.

from tmpy.graph.pdflatex import PDFLaTeX
from tmpy.protocol import flush_err

PRE_CODE = """
\\documentclass[tikz]{standalone}
\\begin{document}
"""

POST_CODE = """
\\end{document}
"""


class TikZ(PDFLaTeX):
    """
    TikZ support
    """

    def __init__(self, name="tikz"):
        super().__init__()
        self.name = name
        self.message = "TeXmacs interface to TikZ"

    def available(self):
        if not super().available():
            return False
        for sty in ("standalone", "tikz"):
            if len(super().kpsewhich(sty + ".sty")) <= 0:
                flush_err(
                    "Failed to find " + sty + ".sty,"
                    " please install the missing LaTeX packages\n"
                )
                return False
        return True

    def evaluate(self, code):
        if not code.lstrip().startswith("\\documentclass"):
            if code.lstrip().startswith("\\usetikzlibrary"):
                pass
            elif not code.lstrip().startswith("\\begin{tikzpicture}"):
                code = "\\begin{tikzpicture}\n" + code + "\n\\end{tikzpicture}"
            code = PRE_CODE + "\n" + code + "\n" + POST_CODE

        super().evaluate(code)
