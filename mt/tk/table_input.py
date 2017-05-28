
import logging
import collections
import tkinter as ti
from tkinter import ttk

import mt.str
import mt.dt
import mt.tk.table

def _on_select(i):
    logging.debug('Entry with ID "'+i+'" selected.')

def _prepare(d):
    if mt.str.is_str(d):
        return d
    if mt.dt.is_dt(d):
        return d.strftime('%Y-%m-%d %H:%M')
    return str(d)

def create(p):
    frame = p['frame']

    left = ttk.Frame(frame)
    right = ttk.Frame(frame)
    entries = collections.OrderedDict()
    data = p['read_all']()

    left.grid(column=0, row=0, sticky=(ti.N, ti.S, ti.W, ti.E))
    right.grid(column=1, row=0, sticky=(ti.N, ti.S, ti.W, ti.E))

    for d in data:
        entries[d['id']] = []
        for i in p['id_to_titles']:
            entries[d['id']].append(_prepare(d[i]))

    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.rowconfigure(0, weight=1)

    left.columnconfigure(0, weight=1)
    left.rowconfigure(0, weight=1)

    right.columnconfigure(0, weight=1)
    right.rowconfigure(0, weight=1)

    mt.tk.table.create({
            'on_select': _on_select,
            'frame': left,
            'sel_id': '',
            'titles': p['id_to_titles'].values(),
            'entries': entries
        })

    return None # Add useful return value?
