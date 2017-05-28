
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

def create(nb):
    return ec.ui.tk.nb_content.create({
        'nb': nb,
        'title': 'Clients',
        'id_to_titles': collections.OrderedDict([
            ('company', 'Company'),
            ('lastname', 'Lastname'),
            ('firstname', 'Firstname')]),
        'read_all': _read_all
    })
