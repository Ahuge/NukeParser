__author__ = 'Alex'
import os

import functions
from parse import ParseKnobs
from __classes__ import Knob


def create_knob(clsname, dct):
    return KnobBuilder(clsname, tuple([Knob]), dct)


def create_knobs(node):
    path = os.path.join(os.path.dirname(__file__), "documentation", "_default", node+".txt")
    knobs = ParseKnobs(path)

    out_knobs = {}
    knobs = list(knobs)
    for knob in knobs:
        name, class_type, value = knob

        out_knobs[name] = create_knob(class_type, {"_value": value if value != "None" else None})()

    return out_knobs


class KnobBuilder(type):
    def __new__(mcs, clsname, bases, dct):
        new_dct = {}
        for func in functions.__knob__:
            name = func.__name__
            if name.startswith("knob_"):
                # One of ours
                new_dct[name[5:]] = func

        for key, value in dct.iteritems():
            new_dct[key] = value

        return super(KnobBuilder, mcs).__new__(mcs, clsname,bases, new_dct)


class NodeBuilder(type):
    def __new__(mcs, clsname, bases, dct):
        new_dct = {}
        for func in functions.__node__:
            name = func.__name__
            if name.startswith("node_"):
                # One of ours
                new_dct[name[5:]] = func

        new_dct['_knobs'] = create_knobs(clsname)

        for key, value in dct.iteritems():
            if key in new_dct['_knobs']:
                new_dct['_knobs'][key].setValue(value)

        return super(NodeBuilder, mcs).__new__(mcs, clsname, tuple([bases]), new_dct)
