
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
    companies = ec.db.company.read_all() # Overdone
    companies = ec.db.get_ordered_id_dict(companies)

    for row in data:
        row['company'] = companies[row['company_id']]['title']
        #del row['company_id']

    data = sorted(data, key=_get_sort_key)
    print(data)
    return data

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
