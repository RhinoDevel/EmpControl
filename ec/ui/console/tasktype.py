
import collections
import ec.db.tasktype
import ec.ui.console

menu_title = 'TASK TYPE'

def _print():
    l = ec.db.tasktype.read_all()
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
            'title': menu_title,
            'entries': collections.OrderedDict([
                ('title', 'Title')]),
            'func': ec.db.tasktype.create
        })

def _modify():
    ec.ui.console.modify(
        {
            'title': menu_title,
            'entries': collections.OrderedDict([
                ('title', 'Title')]),
            'read': ec.db.tasktype.read_by_id,
            'modify': ec.db.tasktype.update_by_id
        })

def _delete():
    ec.ui.console.delete(
        {
            'title': menu_title,
            'func': ec.db.tasktype.delete_by_id
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
