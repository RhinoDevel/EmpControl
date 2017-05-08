
import collections
import ec.ui.console

def menu():
    ec.ui.console.enter_menu(
        {
            "title": "MAIN",
            "entries": collections.OrderedDict([
                    ("p",
                    {
                        "title": "Print",
                        "func": None
                    }),
                    ("c",
                    {
                        "title": "Create",
                        "func": None
                    }),
                    ("m",
                    {
                        "title": "Modify",
                        "func": None
                    }),
                    ("d",
                    {
                        "title": "Delete",
                        "func": None
                    })])
        })
