__author__ = 'Alex'


def __filter(name):
    if name[0] == "_":
        return False
    return True


##############################################################
#                       Node Functions                       #
##############################################################


def node_knob(self, val):
    return self._knobs[val]


def node_knobs(self):
    return self._knobs.keys()


def node_add(self, key, val):
    self._knobs[key] = val


def node___getitem__(self, key):
    return self._knobs[key]


##############################################################
#                       Knob Functions                       #
##############################################################


def knob_value(self):
    return self._value


def knob_setValue(self, value):
    self._value = value

__knob__ = []
__node__ = []

mod = __import__(__name__)
for f in dir(mod):
    if f.startswith("knob"):
        __knob__.append(getattr(mod, f))
    elif f.startswith("node"):
        __node__.append(getattr(mod, f))

__all__ = __knob__ + __node__
