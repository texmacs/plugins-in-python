#!/usr/bin/env python

# MODULE      : tikz.py
# DESCRIPTION : Launcher for the TikZ plugin
# COPYRIGHT   : (C) 2019  Darcy Shen
#
# This software falls under the GNU general public license version 3 or later.
# It comes WITHOUT ANY WARRANTY WHATSOEVER. For details, see the file LICENSE
# in the root directory or <http://www.gnu.org/licenses/gpl-3.0.html>.

from tmpy.protocol import flush_prompt

from tmpy.graph.tikz import TikZ

current = TikZ()
current.greet()
flush_prompt(current.name + "] ")

current.main_loop()
