#!/usr/bin/env python
#
# MODULE      : tm_sympy.py
# DESCRIPTION : Launcher for the SymPy plugin
# COPYRIGHT   : (C) 2019  Darcy Shen
#
# This software falls under the GNU general public license version 3 or later.
# It comes WITHOUT ANY WARRANTY WHATSOEVER. For details, see the file LICENSE
# in the root directory or <http://www.gnu.org/licenses/gpl-3.0.html>.

import sys

from tmpy.capture import CaptureStdout
from tmpy.completion import complete, parse_complete_command
from tmpy.postscript import ps_out
from tmpy.protocol import (
    DATA_COMMAND,
    flush_latex,
    flush_prompt,
    flush_scheme,
    flush_verbatim,
)

try:
    import sympy
    from sympy import Basic, MatrixBase
    from sympy.printing import latex
except ModuleNotFoundError:
    flush_verbatim("Please install sympy first, for example:\n")
    flush_verbatim("    pip install sympy")
    flush_prompt("dead] ")
    sys.exit(0)

import platform

my_globals = {}

# We insert into the session's namespace the 'ps_out' method.
my_globals["ps_out"] = ps_out

# As well as some documentation.
my_globals["__doc__"] = """A SymPy plugin for TeXmacs."""


def flush_output(data):
    if isinstance(data, Basic) or isinstance(data, MatrixBase):
        flush_latex(latex(data))
    else:
        flush_verbatim(str(data).strip())


###############################################################################
# Session start
###############################################################################
flush_verbatim(
    "SymPy %s under Python %s\n"
    % (sympy.__version__, platform.python_version())
)
flush_verbatim("Please see the documentation in Help -> Plugins -> SymPy\n")
flush_prompt(">>> ")

while True:
    line = input()
    if not line:
        continue
    if line[0] == DATA_COMMAND:
        sf = parse_complete_command(line[1:])
        if sf[0] == "complete":
            flush_scheme(complete(sf[1], sf[2], my_globals))
        continue

    lines = [line]
    while line != "<EOF>":
        line = input()
        if line == "":
            continue
        lines.append(line)
    text = "\n".join(lines[:-1])
    try:  # Is it an expression?
        result = eval(text, my_globals)
    except Exception:
        result = CaptureStdout.capture(text, my_globals, "main")
    flush_output(result)
