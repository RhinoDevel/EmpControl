
import collections
import ec.ui.console.company

def enter_menu(data):
    while True:
        s = ""

        print("*** "+data["title"]+" MENU ***")
        for k, v in data["entries"].items():
            print(k+" "+v["title"])
        print("X"+" "+"Exit")

        s = input("Please select"+":"+" ")
        if s=="X":
            break
        if s in data["entries"]:
            data["entries"][s]["func"]()
        else:
            print("Unknown command.")

def menu():
    enter_menu(
        {
            "title": "MAIN",
            "entries": collections.OrderedDict([
                    ("c",
                    {
                        "title": "Companies",
                        "func": ec.ui.console.company.menu
                    })])
        })
