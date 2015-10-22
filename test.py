import os
from create_class import create_node
from parse import ParseNk

PATH = os.path.join(os.path.dirname(__file__), "nodes.nk")

nodes = ParseNk(PATH)
node_types = []

for node in nodes:

    if "_CLASS" in node:
        __class = node["_CLASS"]
        del node['_CLASS']
        node_class = create_node(__class, node)
        if node_class not in node_types:
            node_types.append(node_class)

print node_types

s = node_types[0]

MyBackdrop = s()

print MyBackdrop['name']
print MyBackdrop['name'].value()
print MyBackdrop.knobs()