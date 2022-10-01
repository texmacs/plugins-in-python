#
# MODULE      : complete.py
# DESCRIPTION : Complete implemented in Python
# COPYRIGHT   : (C) 2019  Darcy Shen
#
# This software falls under the GNU general public license version 3 or later.
# It comes WITHOUT ANY WARRANTY WHATSOEVER. For details, see the file LICENSE
# in the root directory or <http://www.gnu.org/licenses/gpl-3.0.html>.

from tmpy.protocol import DATA_COMMAND, flush_scheme, flush_verbatim

flush_verbatim("We know how to complete 'h'")

while True:
    line = input()
    if not line:
        pass
    if line[0] == DATA_COMMAND:
        flush_scheme("""(tuple "h" "ello" "i there" "ola" "opsakee")""")
    else:
        flush_verbatim("You typed " + line)
