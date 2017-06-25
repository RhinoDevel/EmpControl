
import logging
import collections
import tkinter as ti
from tkinter import ttk

import mt.str
import mt.dt
import mt.tk
import mt.tk.table_input

def _on_select(i):
    logging.debug('Entry with ID "'+i+'" selected.')

def _recreate(p):
    mt.tk.clear_frame(p['frame'])

    mt.tk.table_input.create(p)

    if 'on_recreate' in p:
        p['on_recreate']()

def _update(d, p, update):
    update(d) # TODO: Add error handling.
    _recreate(p)

def _create(d, p, create):
    create(d) # TODO: Add error handling.
    _recreate(p)

def _delete(i, p, delete):
    # TODO: Add modal dialog asking user, if deletion is really wanted.
    delete(i) # TODO: Add error handling.
    _recreate(p)

def create(p):
    """Create notebook page content.

    Alters given parameters dictionary!

    Returns altered parameters dictionary.
    """

    p['frame'] = ttk.Frame(p['nb'])
    p['update'] = lambda d, p = p, update = p['update']: _update(d, p, update)
    p['create'] = lambda d, p = p, create = p['create']: _create(d, p, create)
    p['delete'] = lambda i, p = p, delete = p['delete']: _delete(i, p, delete)
    p['recreate'] = lambda p = p: _recreate(p)

    _recreate(p)

    p['nb'].add(p['frame'], text=p['title'])

    return p
