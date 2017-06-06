
import collections

import ec.db.worker
import ec.ui.tk.nb_content

def create(nb):
    return ec.ui.tk.nb_content.create({
        'nb': nb,
        'title': 'Workers',
        'id_to_data': collections.OrderedDict([
            ('lastname', {'title': 'Lastname'}),
            ('firstname', {'title': 'Firstname'})]),
        'read_all': ec.db.worker.read_all,
        'update': ec.db.worker.update_by_id,
        'create': ec.db.worker.create,
        'delete': ec.db.worker.delete_by_id
    })
