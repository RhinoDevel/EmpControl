
import collections
import operator

import mt.str

import ec.db
import ec.db.workday
import ec.db.worker
import ec.ui.tk.nb_content

last_data = None
last_worker_values = []
last_worker_titles = []

def _get_sort_key(d):
    return (d['worker'])

def _read_all():
    global last_data
    global last_worker_values
    global last_worker_titles

    last_data = ec.db.workday.read_all()
    del last_worker_values[:]
    del last_worker_titles[:]
    workers = ec.db.get_ordered_id_dict(ec.db.worker.read_all())

    for row in last_data:
        row['worker'] = mt.str.get_name_str(
            workers[row['worker_id']]['lastname'],
            workers[row['worker_id']]['firstname'])

    last_data = sorted(last_data, key=_get_sort_key)

    # Update worker select data:
    #
    for k, v in workers.items():
        if k in last_worker_values:
            continue;
        last_worker_values.append(k)
        last_worker_titles.append(
            mt.str.get_name_str(v['lastname'], v['firstname']))

    return last_data

def _get_val_from_id(i):
    # Probably a stupid way to do this:
    #
    for e in last_data:
        if e['id']==i:
            return e['worker_id']

    return None # Must not happen.

def create(nb):
    # Get data for worker select:
    #
    global last_data
    global last_worker_values
    global last_worker_titles
    last_data = _read_all() # Also updates last_... variables.

    return ec.ui.tk.nb_content.create({
        'nb': nb,
        'title': 'Workdays',
        'id_to_data': collections.OrderedDict([
            (
                'worker',
                {
                    'title': 'Worker',
                    'type': 'sel',
                    'values': last_worker_values,
                    'titles': last_worker_titles,
                    'get_val_from_id': _get_val_from_id,
                    'val_id': 'worker_id'
                }
            )]),
        'read_all': _read_all,
        'update': ec.db.workday.update_by_id,
        'create': ec.db.workday.create,
        'delete': ec.db.workday.delete_by_id
    })
