
import collections

import ec.db.company
import ec.ui.tk.nb_content

def create(nb):
    return ec.ui.tk.nb_content.create({
        'nb': nb,
        'title': 'Companies',
        'id_to_titles': collections.OrderedDict([('title', 'Titles')]),
        'read_all': ec.db.company.read_all
    })
