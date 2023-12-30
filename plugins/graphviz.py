#!/usr/bin/env python

# MODULE      : tm_graphviz.py
# DESCRIPTION : Launcher for the Graphviz plugin
# COPYRIGHT   : (C) 2019  Darcy Shen
#
# This software falls under the GNU general public license version 3 or later.
# It comes WITHOUT ANY WARRANTY WHATSOEVER. For details, see the file LICENSE
# in the root directory or <http://www.gnu.org/licenses/gpl-3.0.html>.

from tmpy.protocol import DATA_COMMAND, flush_prompt, flush_verbatim

from tmpy.graph.graphviz import Graphviz

graphs = list(
    map(
        lambda x: Graphviz(x),
        ["dot", "neato", "twopi", "circo", "fdp", "sfdp", "patchwork", "osage"],
    )
)
graph_names = list(map(lambda x: x.name, graphs))

if len(graphs) == 0:
    flush_verbatim("\nSorry, please check your installation of Graphviz")
    flush_prompt("dead] ")
    exit(0)

current = graphs[0]
current.greet()
flush_prompt(current.name + "] ")


def unigraph(text):
    magic_lines = text.split("\n")
    magic_line = magic_lines[0]
    command = magic_line.split(" ")[0].strip("%")

    if command in graph_names:
        graph = graphs[graph_names.index(command)]
        graph.eval(text)
    else:
        flush_verbatim("No such Graphs backend: " + command)


# Main session loop.
while True:
    line = input()
    if not line:
        continue
    if line[0] == DATA_COMMAND:
        # TODO: Handle completions
        continue
    else:
        lines = [line]
        while line != "<EOF>":
            line = input()
            if line == "":
                continue
            lines.append(line)

        text = "\n".join(lines[:-1])

        if text.startswith("%"):
            unigraph(text)
        elif text == "help":
            flush_verbatim("[help, " + ", ".join(str(x) for x in graph_names) + "]\n")
            current.greet()
        elif text in graph_names:
            current = graphs[graph_names.index(text)]
            current.greet()
        else:
            current.eval(text)
