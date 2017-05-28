
import collections

import ec.db.tasktype
import ec.ui.tk.nb_content

def create(nb):
    return ec.ui.tk.nb_content.create({
        'nb': nb,
        'title': 'Task Types',
        'id_to_titles': collections.OrderedDict([('title', 'Title')]),
        'read_all': ec.db.tasktype.read_all
    })
