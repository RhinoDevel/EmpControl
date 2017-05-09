
import collections
import ec.db.company
import ec.ui.console

def _print():
    l = ec.db.company.read_all()
    if not l:
        print("No entries.")
        return

    for v in l:
        print(v['title']) # Hard-coded

def _create():
    ec.ui.console.create(
        {
            'title': 'COMPANY',
            'entries': collections.OrderedDict([
                ('title', 'Title')]),
            'func': ec.db.company.create
        })

def menu():
    ec.ui.console.enter_menu(
        {
            'title': 'MAIN',
            'entries': collections.OrderedDict([
                    ('p',
                    {
                        'title': 'Print',
                        'func': _print
                    }),
                    ('c',
                    {
                        'title': 'Create',
                        'func': _create
                    }),
                    ('m',
                    {
                        'title': 'Modify',
                        'func': None
                    }),
                    ('d',
                    {
                        'title': 'Delete',
                        'func': None
                    })])
        })
