__author__ = 'Alex'

from __classes__ import Node
from meta import NodeBuilder


def create_node(clsname, args):

    return NodeBuilder(clsname, Node, args)
