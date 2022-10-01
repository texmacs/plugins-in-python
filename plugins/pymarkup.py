#
# MODULE      : pymarkup.py
# DESCRIPTION : Example plugin `markup` implemented in Python
# COPYRIGHT   : (C) 2022  Darcy Shen
#
# This software falls under the GNU general public license version 3 or later.
# It comes WITHOUT ANY WARRANTY WHATSOEVER. For details, see the file LICENSE
# in the root directory or <http://www.gnu.org/licenses/gpl-3.0.html>.

from tmpy.protocol import flush_latex, flush_verbatim

flush_verbatim("Enter a LaTeX expression at each prompt")

while True:
    line = input()
    if not line:
        pass
    else:
        flush_latex("\\foo{" + line + "}")
