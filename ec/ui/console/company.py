
import collections
import ec.db.company
import ec.ui.console

def _print():
    l = ec.db.company.read_all()
    if not l:
        print('No entries.')
        return

    print('ID      ' + ' | ' + 'Title')
    print('--------' + '---' + '--------')
    for v in l:
        print(v['id'], end=' | ')
        print(v['title'])

def _create():
    ec.ui.console.create(
        {
            'title': 'COMPANY',
            'entries': collections.OrderedDict([
                ('title', 'Title')]),
            'func': ec.db.company.create
        })

def _modify():
    ec.ui.console.modify(
        {
            'title': 'COMPANY',
            'entries': collections.OrderedDict([
                ('title', 'Title')]),
            'read': ec.db.company.read_by_id,
            'modify': ec.db.company.update_by_id
        })

def _delete():
    ec.ui.console.delete(
        {
            'title': 'COMPANY',
            'func': ec.db.company.delete_by_id
        })

def menu():
    ec.ui.console.enter_menu(
        {
            'title': 'COMPANY',
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
                    'func': _modify
                }),
                ('d',
                {
                    'title': 'Delete',
                    'func': _delete
                })])
        })
