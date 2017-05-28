
import logging
import collections
import tkinter as ti
from tkinter import ttk

import mt.str
import mt.dt
import mt.tk.table_input

def _on_select(i):
    logging.debug('Entry with ID "'+i+'" selected.')

def _prepare(d):
    if mt.str.is_str(d):
        return d
    if mt.dt.is_dt(d):
        return d.strftime('%Y-%m-%d %H:%M')
    return str(d)

def _update(d, update):
    update(d) # TODO: Add error handling.
    # TODO: Implement re-reading ALL from DB and updating UI.

def create(p):
    """Create notebook page content.

    Alters given parameters dictionary!
    """

    p['frame'] = ttk.Frame(p['nb'])

    p['update'] = lambda d, update = p['update']: _update(d, update)

    mt.tk.table_input.create(p)

    p['nb'].add(p['frame'], text=p['title'])

    return None # Add useful return value?
