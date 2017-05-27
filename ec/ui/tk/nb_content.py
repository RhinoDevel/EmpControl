
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
    frame = ttk.Frame(p['nb'])
    entries = collections.OrderedDict()
    data = p['read_all']()

    for d in data:
        entries[d['id']] = []
        for i in p['id_to_titles']:
            entries[d['id']].append(_prepare(d[i]))

    p['nb'].add(frame, text=p['title'])
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)

    return mt.tk.table.create({
            'on_select': _on_select,
            'frame': frame,
            'sel_id': '',
            'titles': p['id_to_titles'].values(),
            'entries': entries
        })
