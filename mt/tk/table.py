
import logging
import tkinter as ti
from tkinter import ttk

border_cell = 5
pad_table = 5
col_bg_table = 'blue'
col_bg_row_deselected = 'red'
col_bg_row_selected = 'yellow'

# TODO: Implement scrolling.

def _deselect_row(o, r):
    for col_ele in o['ele'][r]:
        col_ele.configure(background=col_bg_row_deselected)

def _select_row(o, r):
    logging.debug('Selecting row at index '+str(r)+'..')

    for i, row_eles in enumerate(o['ele']):
        if i==r:
            for col_ele in row_eles:
                col_ele.configure(background=col_bg_row_selected)
        else:
            _deselect_row(o, i)

def _deselect_wo_call(o, i, r):
    _deselect_row(o, r)
    o['sel_id'] = None

def _select_wo_call(o, i, r):
    _select_row(o, r)
    o['sel_id'] = i

def _select_toggle(o, i, r):
    if i==o['sel_id']:
        _deselect_wo_call(o, i, r)
        if callable(o['on_deselect']):
            o['on_deselect'](i)
    else:
        _select_wo_call(o, i, r)
        if callable(o['on_select']):
            o['on_select'](i)

def _on_click_row(o, i, r, e):
    logging.debug('ID of clicked row at index '+str(r)+' is "'+i+'"."')

    _select_toggle(o, i, r)

def _add_cell(o, col, row, i, text, is_title):
    label = ttk.Label(o['frame'], text=text, border=border_cell)

    label.grid(column=col, row=row, sticky=(ti.N, ti.S, ti.W, ti.E))

    if is_title:
        label.configure(font='bold')
    else:
        label.bind(
            "<Button-1>", lambda e, i=i, o=o, r=row: _on_click_row(o, i, r, e))

    o['ele'][row].append(label)

    label.configure(background=col_bg_row_deselected)

def _add_row(o, row, i, texts, are_titles):
    col = 0
    o['ele'].append([])
    for text in texts:
        _add_cell(o, col, row, i, text, are_titles)
        col = col+1

def create(p):
    o = {
        'frame': ttk.Frame(p['frame']),
        'on_deselect': p['on_deselect'],
        'on_select': p['on_select'],
        'ele': [],
        'sel_id': p['sel_id']
    }

    o['frame'].grid(
        column=0,
        row=0,
        padx=pad_table,
        pady=pad_table,
        sticky=(ti.N, ti.S, ti.W, ti.E))

    row = 0
    sel_row = -1

    _add_row(o, row, None, p['titles'], True)
    row = row+1

    for k, v in p['entries'].items():
        _add_row(o, row, k, v, False)
        if o['sel_id'] and k==o['sel_id']:
            sel_row = row # It would be possible to do without this..
        row = row+1

    if sel_row!=-1:
        _select_wo_call(o, o['sel_id'], sel_row)

    ttk.Style().configure('MTtable.TFrame', background=col_bg_table)
    o['frame'].configure(style='MTtable.TFrame')

    return o
