
import collections
import operator

import ec.db
import ec.db.client
import ec.db.company
import ec.ui.tk.nb_content

last_data = None
last_company_values = []
last_company_titles = []

def _get_sort_key(d):
    return (d['company'], d['lastname'], d['firstname'])

def _read_all():
    global last_data
    global last_company_values
    global last_company_titles

    last_data = ec.db.client.read_all()
    del last_company_values[:]
    del last_company_titles[:]
    companies = ec.db.get_ordered_id_dict(ec.db.company.read_all())

    for row in last_data:
        row['company'] = companies[row['company_id']]['title']

    last_data = sorted(last_data, key=_get_sort_key)

    # Update company select data:
    #
    for k, v in companies.items():
        if k in last_company_values:
            continue;
        last_company_values.append(k)
        last_company_titles.append(v['title'])

    return last_data

def _get_val_from_id(i):
    # Probably a stupid way to do this:
    #
    for e in last_data:
        if e['id']==i:
            return e['company_id']

    return None # Must not happen.

def create(nb):
    # Get data for company select:
    #
    global last_data
    global last_company_values
    global last_company_titles
    last_data = _read_all() # Also updates last_... variables.

    return ec.ui.tk.nb_content.create({
        'nb': nb,
        'title': 'Clients',
        'id_to_data': collections.OrderedDict([
            (
                'company',
                {
                    'title': 'Company',
                    'type': 'sel',
                    'values': last_company_values,
                    'titles': last_company_titles,
                    'get_val_from_id': _get_val_from_id,
                    'val_id': 'company_id'
                }
            ),
            ('lastname', {'title': 'Lastname', 'type': 'str'}),
            ('firstname', {'title': 'Firstname', 'type': 'str'})]),
        'read_all': _read_all,
        'update': ec.db.client.update_by_id,
        'create': ec.db.client.create,
        'delete': ec.db.client.delete_by_id
    })
