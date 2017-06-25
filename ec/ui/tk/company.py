
import collections

import ec.db.company
import ec.ui.tk.nb_content

def create(nb, client_recreate=None):
    p = {
        'nb': nb,
        'title': 'Companies',
        'id_to_data': collections.OrderedDict([
            ('title', {'title': 'Title', 'type': 'str'})]),
        'read_all': ec.db.company.read_all,
        'update': ec.db.company.update_by_id,
        'create': ec.db.company.create,
        'delete': ec.db.company.delete_by_id
    }

    if client_recreate:
        p['on_recreate'] = client_recreate

    return ec.ui.tk.nb_content.create(p)
