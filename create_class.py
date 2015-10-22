__author__ = 'Alex'

from __classes__ import Node
from meta import NodeBuilder


def create_node(clsname, args):

    new_class = NodeBuilder(clsname, Node, args)
    return new_class
