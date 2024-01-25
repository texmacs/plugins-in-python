#!/usr/bin/env python
###############################################################################
##
## MODULE      : pdflatex.py
## DESCRIPTION : LaTeX graphics support
## COPYRIGHT   : (C) 2019  Darcy Shen and Massimiliano Gubinelli
##
## This software falls under the GNU general public license version 3 or later.
## It comes WITHOUT ANY WARRANTY WHATSOEVER. For details, see the file LICENSE
## in the root directory or <http://www.gnu.org/licenses/gpl-3.0.html>.

import os
import shutil
from subprocess import Popen, PIPE, STDOUT
from tmpy.graph.graph import Graph
from tmpy.protocol import flush_file, flush_err, flush_verbatim


class PDFLaTeX(Graph):
    """
    TeXmacs interface to PDFLaTeX for picture generation
    """

    def __init__(self, name="pdflatex"):
        super().__init__()
        self.name = name
        self.cmd = "pdflatex"
        self.message = "TeXmacs interface to PDFLaTeX for picture generation"

    def available(self):
        return shutil.which(self.cmd) is not None

    def greet(self):
        if not self.message:
            try:
                with Popen([self.cmd, "--version"], stderr=PIPE) as p:
                    out, err = p.communicate()
                    if p.returncode == 0:
                        self.message = err.decode()
                    else:
                        self.message = out
            except OSError:
                pass
        super().greet()

    def kpsewhich(self, name):
        """use kpsewhich to find latex package."""
        cmd = ["kpsewhich", name]
        with Popen(cmd, stdout=PIPE, stderr=STDOUT) as p:
            out, _err = p.communicate()
            if p.returncode == 0:
                return out
        return ""

    def evaluate(self, code):
        if not code.lstrip().startswith("\\documentclass"):
            flush_err(
                "I expect a valid LaTeX document, usually starting with\n"
                + "   \\documentclass{standalone}\n"
                + "which will take proper care of suitable bounding box for the image.\n"
                + "The document is sent to latex and then to dvips to produce a single image."
            )
            flush_verbatim("")
            return

        code_path = self.get_tmp_dir() + self.name + ".tex"
        pdf_path = self.get_tmp_dir() + self.name + ".pdf"

        with open(code_path, "wb") as code_file:
            code_file.write(code.encode())

        args = [
            self.cmd,
            "--interaction=errorstopmode",
            "-halt-on-error",
            code_path,
        ]

        # flush_err (code) # to debug
        phase = "PDFLaTeX"
        # flush_err ("Running " + phase)
        os.chdir(self.get_tmp_dir())
        with Popen(args, stdout=PIPE, stderr=STDOUT) as p:
            out, _err = p.communicate()
            if p.returncode == 0:
                phase = "Finished"
                # flush_err ("Running " + phase)
                size_param = f"?width={self.width}&height={self.height}"
                flush_file(pdf_path + size_param)
                return
            flush_err(phase + " error!\n" + out.decode())
            flush_verbatim("")  # otherwise TeXmacs keeps waiting output
