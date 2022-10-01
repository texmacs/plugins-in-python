#!/usr/bin/env python

# MODULE      : pyprompt.py
# DESCRIPTION : Prompt implemented in Python
# COPYRIGHT   : (C) 2019  Darcy Shen
#
# This software falls under the GNU general public license version 3 or later.
# It comes WITHOUT ANY WARRANTY WHATSOEVER. For details, see the file LICENSE
# in the root directory or <http://www.gnu.org/licenses/gpl-3.0.html>.


from tmpy.protocol import flush_latex, flush_prompt, flush_verbatim

flush_verbatim("A LaTeX -> TeXmacs converter")

counter = 0
while True:
    counter = counter + 1
    flush_prompt("Input " + str(counter) + "] ")
    line = input()
    if not line:
        pass
    else:
        flush_latex(line)
