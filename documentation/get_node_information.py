try:
    import nuke
    import nukescripts
except ImportError:
    print "Cannot import nuke libraries. Good luck."
import os

node_dic = {}


def getItem(menu):
    """
    Recursive function to browse all menus and submenus
    of the Nodes menu to retrieve all items and commands
    to execute them.
    """
    if isinstance(menu,nuke.Menu):
        for item in menu.items():
            if item.name() in ["Other", "All plugins"] or len(menu.name()) == 1 or len(item.name()) == 1:
                getItem(item)
    else:
        # The menu is actually a command.
        if menu.name() not in node_dic.values():
            node_dic[menu] = menu.name()


getItem(nuke.menu("Nodes"))

path = os.path.join(os.path.dirname(__file__), "_default")

for name in node_dic.values():
    try:
        node = nuke.createNode(name)
        with open(path+r"\%s.txt" % name, "wb") as fh:
            fh.write("")
        with open(path+r"\%s.txt" % name, "a") as fh:
            for knob in node.knobs().values():
                words = " ".join([knob.name(),
                                  knob.Class(),
                                  str(knob.defaultValue()) if hasattr(knob, "defaultValue") else "None"])
                words += "\n"
                fh.write(words)
    
        nukescripts.node_delete(popupOnError=True)
    except Exception:
        print "Could not create documentation for %s" % name
