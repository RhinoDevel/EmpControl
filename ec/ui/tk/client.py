
# TODO: Fix BUG: 1) Create new entry. 2) Select new entry. => ERROR!

import collections
import operator

import ec.db
import ec.db.client
import ec.db.company
import ec.ui.tk.nb_content

def _get_sort_key(d):
    return (d['company'], d['lastname'], d['firstname'])

def _read_all():
    data = ec.db.client.read_all()
    companies = ec.db.get_ordered_id_dict(ec.db.company.read_all())

    for row in data:
        row['company'] = companies[row['company_id']]['title']

    return sorted(data, key=_get_sort_key)

def _get_val_from_id(i, d):
    # Probably a stupid way to do this:
    #
    for e in d:
        if e['id']==i:
            return e['company_id']

    return None # Must not happen.

def create(nb):
    # Get data for company select:
    #
    data = _read_all()
    company_values = []
    company_titles = []
    for e in data:
        if e['company_id'] in company_values:
            continue;
        company_values.append(e['company_id'])
        company_titles.append(e['company'])

    return ec.ui.tk.nb_content.create({
        'nb': nb,
        'title': 'Clients',
        'id_to_data': collections.OrderedDict([
            (
                'company_id', # TODO: Fix this!
                {
                    'title': 'Company',
                    'type': 'sel',
                    'values': company_values,
                    'titles': company_titles,
                    'get_val_from_id': lambda i, d=data: _get_val_from_id(i, d)
                }
            ),
            ('lastname', {'title': 'Lastname', 'type': 'str'}),
            ('firstname', {'title': 'Firstname', 'type': 'str'})]),
        'read_all': _read_all,
        'update': ec.db.client.update_by_id,
        'create': ec.db.client.create,
        'delete': ec.db.client.delete_by_id
    })
