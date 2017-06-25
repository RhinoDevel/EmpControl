
import logging
import collections
import tkinter as ti
from tkinter import ttk

import mt.str
import mt.dt
import mt.tk.table
import mt.tk.input

def _on_deselect(i, ordered_ids, input_o):
    for k in ordered_ids: # Set variable connected to input element.
        input_o['var_and_eles'][k]['clear']()

    input_o['id'] = '' # Hard-coded

def _on_select(i, ordered_ids, entries, input_o):
    logging.debug('Entry with ID "'+i+'" selected.')

    j = 0 # = Index of entries (equals index of ordered_ids).
    for k in ordered_ids: # Set variable connected to input element.
        input_o['var_and_eles'][k]['set'](i, entries[i][j])
        j = j+1

    input_o['id'] = i

def _on_apply(input_o, update, create):
    func = create
    d = {}

    if(input_o['id']):
        func = update
        d['id'] = input_o['id']

    for k, v in input_o['var_and_eles'].items():
        d[k] = v['var'].get()

    func(d)

def _on_delete(i, delete):
    delete(i)

def _prepare(d):
    if mt.str.is_str(d):
        return d
    if mt.dt.is_dt(d):
        return d.strftime('%Y-%m-%d %H:%M')
    return str(d)

def create(p):
    frame = p['frame']
    input_o = None
    table_o = None

    left = ttk.Frame(frame)
    right = ttk.Frame(frame)
    entries = collections.OrderedDict()
    data = p['read_all']()

    left.grid(column=0, row=0, sticky=(ti.N, ti.S, ti.W, ti.E))
    right.grid(column=1, row=0, sticky=(ti.N, ti.S, ti.W, ti.E))

    for d in data:
        entries[d['id']] = []
        for i in p['id_to_data']:
            entries[d['id']].append(_prepare(d[i]))

    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.rowconfigure(0, weight=1)

    left.columnconfigure(0, weight=1)
    left.rowconfigure(0, weight=1)

    right.columnconfigure(0, weight=1)
    right.rowconfigure(0, weight=1)

    input_o = mt.tk.input.create({
            'frame': right,
            'id_to_data': p['id_to_data'],
            'on_apply': lambda
                input_o_then,
                update=p['update'],
                create=p['create']: _on_apply(input_o_then, update, create)
        })

    table_o = mt.tk.table.create({
            'on_deselect': lambda
                i,
                ordered_ids=p['id_to_data'].keys(),
                input_o=input_o: _on_deselect(i, ordered_ids, input_o),
            'on_select': lambda
                i,
                ordered_ids=p['id_to_data'].keys(),
                entries=entries,
                input_o=input_o: _on_select(i, ordered_ids, entries, input_o),
            'on_delete': lambda
                i,
                delete=p['delete']: _on_delete(i, delete),
            'frame': left,
            'sel_id': '',
            'titles': list(map(lambda d: d['title'],p['id_to_data'].values())),
            'entries': entries
        })

    return None # Add useful return value?
