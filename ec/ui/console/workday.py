
import collections
import ec.db.workday
import ec.ui.console

def _print():
    l = ec.db.workday.read_all()
    if not l:
        print('No entries.')
        return

    print('ID        ' + ' | ' + 'Worker ID ' + ' | ' + 'Begin at  ' + ' | ' + 'End at    ' + ' | ' + 'Break     ' + ' | ' + 'Vacation  ' + ' | ' + 'Sick      ')
    print('----------' + '---' + '----------' + '---' + '----------' + '---' + '----------' + '---' + '----------' + '---' + '----------' + '---' + '----------')
    for v in l: # TODO: Fix end strings!
        print(v['id'], end='   | ')
        print(v['worker_id'], end='   | ')
        print(str(v['begin_at']), end='   | ')
        print(str(v['end_at']), end='   | ')
        print(str(v['break']), end='   | ')
        print(str(v['vacation']), end=' | ')
        print(v['sick'])

def _create():
    return # TODO: Implement!

def _modify():
    return # TODO: Implement!

def _delete():
    ec.ui.console.delete(
        {
            'title': 'WORKDAY',
            'func': ec.db.workday.delete_by_id
        })

def menu():
    ec.ui.console.enter_menu(
        {
            'title': 'WORKDAY',
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
