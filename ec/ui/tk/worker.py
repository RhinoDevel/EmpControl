
import collections

import ec.db.worker
import ec.ui.tk.nb_content

def create(nb):
    return ec.ui.tk.nb_content.create({
        'nb': nb,
        'title': 'Workers',
        'id_to_titles': collections.OrderedDict([
            ('lastname', 'Lastname'),
            ('firstname', 'Firstname')]),
        'read_all': ec.db.worker.read_all
    })