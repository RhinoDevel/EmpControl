
import collections

import ec.db.client
import ec.ui.tk.nb_content

def create(nb):
    return ec.ui.tk.nb_content.create({
        'nb': nb,
        'title': 'Clients',
        'id_to_titles': collections.OrderedDict([
            # TODO: Implement company.
            ('lastname', 'Lastname'),
            ('firstname', 'Firstname')]),
        'read_all': ec.db.client.read_all
    })
