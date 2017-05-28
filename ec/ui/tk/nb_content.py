
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

def _recreate(p):
    for widget in p['frame'].winfo_children():
        widget.destroy()

    mt.tk.table_input.create(p)

def _update(d, p, update):
    update(d) # TODO: Add error handling.
    _recreate(p)

def create(p):
    """Create notebook page content.

    Alters given parameters dictionary!
    """

    p['frame'] = ttk.Frame(p['nb'])
    p['update'] = lambda d, p=p, update = p['update']: _update(d, p, update)

    _recreate(p)

    p['nb'].add(p['frame'], text=p['title'])

    return None # Add useful return value?
