#!/usr/bin/env python

# MODULE      : minimal.py
# DESCRIPTION : Minimal implemented in Python
# COPYRIGHT   : (C) 2019  Darcy Shen
#
# This software falls under the GNU general public license version 3 or later.
# It comes WITHOUT ANY WARRANTY WHATSOEVER. For details, see the file LICENSE
# in the root directory or <http://www.gnu.org/licenses/gpl-3.0.html>.

from tmpy.protocol import flush_verbatim

flush_verbatim("Hi there!")

while True:
    line = input()
    if not line:
        pass
    else:
        flush_verbatim("You typed " + line)
