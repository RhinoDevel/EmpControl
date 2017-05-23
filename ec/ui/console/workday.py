
import collections
from datetime import datetime
from datetime import timedelta
import ec.db.workday
import ec.ui.console

def _print():
    l = ec.db.workday.read_all()
    if not l:
        print('No entries.')
        return

    print('ID      ' + ' | ' + 'Worker ID' + ' | ' + 'Begin at                 ' + ' | ' + 'End at                   ' + ' | ' + 'Break' + ', ' + 'Vacation' + ', ' + 'Sick ')
    print('--------' + '---' + '---------' + '---' + '-------------------------' + '---' + '-------------------------' + '---')
    for v in l: # TODO: Fix end strings!
        print(v['id'], end=' | ')
        print(v['worker_id'], end='  | ')
        print(str(v['begin_at']), end=' | ')
        print(str(v['end_at']), end=' | ')
        print(str(v['break']), end=', ')
        print(str(v['vacation']), end=', ')
        print(v['sick'])

def _convert(data):
    data['begin_at'] = datetime.strptime(data['begin_at'], '%Y-%m-%d %H:%M')
    data['end_at'] = datetime.strptime(data['end_at'], '%Y-%m-%d %H:%M')
    data['break'] = timedelta(minutes=int(data['break']))
    data['vacation'] = data['vacation']=='y'
    data['sick'] = data['sick']=='y'

    return data

def _db_create_convert(data):
    ec.db.workday.create(_convert(data))

def _db_modify_convert(data):
    ec.db.workday.update_by_id(_convert(data))

def _create():
    ec.ui.console.create(
        {
            'title': 'WORKDAY',
            'entries': collections.OrderedDict([
                ('worker_id', 'Worker ID'),
                ('begin_at', 'Begin at'),
                ('end_at', 'End at'),
                ('break', 'Break'),
                ('vacation', 'Vacation'),
                ('sick', 'Sick')]),
            'func': _db_create_convert
        })

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
