
import collections

import ec.db.tasktype
import ec.ui.tk.nb_content

def create(nb):
    return ec.ui.tk.nb_content.create({
        'nb': nb,
        'title': 'Task Types',
        'id_to_data': collections.OrderedDict([
            ('title', {'title': 'Title', 'type': 'str'})]),
        'read_all': ec.db.tasktype.read_all,
        'update': ec.db.tasktype.update_by_id,
        'create': ec.db.tasktype.create,
        'delete': ec.db.tasktype.delete_by_id
    })
