__author__ = 'Alex'
import re
import os

NODE_OPEN = re.compile(r"^(\w+)\s\{$")
NODE_CLOSE = re.compile(r"^\}$")
NODE_KV = re.compile(r"^\s(\w+)\s(\w+)$")
KNOB_DEFAULTS = re.compile(r"^(\w+)\s(\w+)\s(\w+)\s?\r?\n?$")


def ParseNk(fp):
    raw_nodes = _yield_nodes(fp)

    nodes = []

    for node in raw_nodes:
        node_args = _make_args(node)
        if "name" in node_args:
            nodes.append(node_args)

    return nodes


def ParseKnobs(fp):
    with open(fp, "rb") as fh:
        lines = fh.readlines()

    for line in lines:
        match = KNOB_DEFAULTS.match(line)
        if match:
            yield match.group(1), match.group(2), match.group(3)


def _make_args(node_line):
    args = {}
    for line in node_line:
        isname = NODE_OPEN.match(line)
        if isname:
            args["_CLASS"] = isname.group(1)

        else:
            kv = NODE_KV.match(line)
            if kv:
                key = kv.group(1)
                val = kv.group(2)

                args[key] = val
    return args



def _yield_nodes(input_file):
    """
    _yield_nodes will yield the nodes from a nuke file. It probably wont work with roto nodes and tracker nodes, but all
    simple nodes should work.
    :param input_file: (str|unicode) Path to the nk file to be parsed.
    :yields:  (list) Lines of the input_file in "node sized" chunks
    """

    open_node = re.compile(r"^\w+\s\{$")
    close_node = re.compile(r"^\}$")

    node = []
    node_status = False

    with open(input_file) as handle:
        for line in iter(lambda: handle.readline(), ""):
            line = line.replace("\n", "")
            if not node_status and re.match(open_node, line):  # If not in a node and a new node opener is found.
                node_status = True

            if node_status:
                node.append(line)
                if re.match(close_node, line):  # Ending of node.
                    node_status = False
                    y_node = node
                    node = []  # Reset the node list
                    yield y_node  # Yield the node list.