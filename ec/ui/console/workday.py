
import collections
from datetime import datetime
from datetime import timedelta
import ec.db.workday
import ec.ui.console
import mt.str

def _print():
    l = ec.db.workday.read_all()
    if not l:
        print('No entries.')
        return

    print('ID      ' + ' | ' + 'Worker ID' + ' | ' + 'Begin at' + ', ' + 'End at' + ', ' + 'Break' + ', ' + 'Vacation' + ', ' + 'Sick ')
    print('--------' + '---' + '---------' + '---')
    for v in l:
        print(v['id'], end=' | ')
        print(v['worker_id'], end='  | ')
        print(str(v['begin_at']), end=', ')
        print(str(v['end_at']), end=', ')
        print(str(v['break']), end=', ')
        print(str(v['vacation']), end=', ')
        print(v['sick'])

def _convert_from_str(data):
    if data['begin_at']=='-':
        data['begin_at'] = None
    else:
        data['begin_at'] = datetime.strptime(data['begin_at'], '%Y-%m-%d %H:%M')
    if data['end_at']=='-':
        data['end_at'] = None
    else:
        data['end_at'] = datetime.strptime(data['end_at'], '%Y-%m-%d %H:%M')
    data['break'] = timedelta(minutes=int(data['break']))
    data['vacation'] = data['vacation']=='y'
    data['sick'] = data['sick']=='y'

    return data

def _convert_to_str(data):
    if data['begin_at'] is None:
        data['begin_at'] = '-'
    else:
        data['begin_at'] = data['begin_at'].strftime('%Y-%m-%d %H:%M')
    if data['end_at'] is None:
        data['end_at'] = '-'
    else:
        data['end_at'] = data['end_at'].strftime('%Y-%m-%d %H:%M')
    data['break'] = str(int(data['break'].seconds/60.0))
    data['vacation'] = 'y' if data['vacation'] else 'n'
    data['sick'] = 'y' if data['sick'] else 'n'

def _db_create_convert(data):
    ec.db.workday.create(_convert_from_str(data))

def _db_modify_convert(data):
    ec.db.workday.update_by_id(_convert_from_str(data))

def _db_read_by_id_convert(i):
    data = ec.db.workday.read_by_id(i)
    _convert_to_str(data)
    return data

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
    ec.ui.console.modify(
        {
            'title': 'WORKDAY',
            'entries': collections.OrderedDict([
                ('worker_id', 'Worker ID'),
                ('begin_at', 'Begin at'),
                ('end_at', 'End at'),
                ('break', 'Break'),
                ('vacation', 'Vacation'),
                ('sick', 'Sick')]),
            'read': _db_read_by_id_convert,
            'modify': _db_modify_convert
        })

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
