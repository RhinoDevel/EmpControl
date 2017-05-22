
import collections
import ec.db.tasktype
import ec.ui.console

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
            'title': 'TASKTYPE',
            'entries': collections.OrderedDict([
                ('title', 'Title')]),
            'func': ec.db.tasktype.create
        })

def _modify():
    ec.ui.console.modify(
        {
            'title': 'TASKTYPE',
            'entries': collections.OrderedDict([
                ('title', 'Title')]),
            'read': ec.db.tasktype.read_by_id,
            'modify': ec.db.tasktype.update_by_id
        })

def _delete():
    ec.ui.console.delete(
        {
            'title': 'TASKTYPE',
            'func': ec.db.tasktype.delete_by_id
        })

def menu():
    ec.ui.console.enter_menu(
        {
            'title': 'TASKTYPE',
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
