
import collections
import ec.db.worker
import ec.ui.console

menu_title = 'WORKER'

def _print():
    l = ec.db.worker.read_all()
    if not l:
        print('No entries.')
        return

    print('ID      ' + ' | ' + 'Lastname' + ', ' + 'Firstname')
    print('--------' + '---')
    for v in l:
        print(v['id'], end=' | ')
        print(v['lastname'], end=', ')
        print(v['firstname'])

def _create():
    ec.ui.console.create(
        {
            'title': menu_title,
            'entries': collections.OrderedDict([
                ('lastname', 'Lastname'),
                ('firstname', 'Firstname')]),
            'func': ec.db.worker.create
        })

def _modify():
    ec.ui.console.modify(
        {
            'title': menu_title,
            'entries': collections.OrderedDict([
                ('lastname', 'Lastname'),
                ('firstname', 'Firstname')]),
            'read': ec.db.worker.read_by_id,
            'modify': ec.db.worker.update_by_id
        })

def _delete():
    ec.ui.console.delete(
        {
            'title': menu_title,
            'func': ec.db.worker.delete_by_id
        })

def menu():
    ec.ui.console.enter_menu(
        {
            'title': menu_title,
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
