
import collections
import ec.db.task
import ec.ui.console

def _print():
    l = ec.db.task.read_all()
    if not l:
        print('No entries.')
        return

    print('ID      ' + ' | ' + 'Workday ID' + ' | ' + 'Type ID ' + ' | ' + 'Client ID' + ' | ' + 'Last edit at' + ', ' + 'Description')
    print('--------' + '---' + '----------' + '---' + '--------' + '---' + '---------' + '---')
    for v in l:
        print(v['id'], end=' | ')
        print(v['workday_id'], end='   | ')
        print(v['type_id'], end=' | ')
        print(v['client_id'], end='  | ')
        print(str(v['lastedit_at']), end=', ')
        print(v['description'])

def _create():
    ec.ui.console.create(
        {
            'title': 'TASK',
            'entries': collections.OrderedDict([
                ('workday_id', 'Workday ID'),
                ('type_id', 'Type ID'),
                ('client_id', 'Client ID'),
                ('description', 'Description')]),
            'func': ec.db.task.create
        })

def _modify():
    ec.ui.console.modify(
        {
            'title': 'TASK',
            'entries': collections.OrderedDict([
                ('workday_id', 'Workday ID'),
                ('type_id', 'Type ID'),
                ('client_id', 'Client ID'),
                ('description', 'Description')]),
            'read': ec.db.task.read_by_id,
            'modify': ec.db.task.update_by_id
        })

def _delete():
    ec.ui.console.delete(
        {
            'title': 'TASK',
            'func': ec.db.task.delete_by_id
        })

def menu():
    ec.ui.console.enter_menu(
        {
            'title': 'TASK',
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
