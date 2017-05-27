
import logging
import tkinter as ti
from tkinter import ttk

border_cell = 5
pad_table = 5
col_bg_table = ''
col_bg_row_deselected = ''
col_bg_row_selected = 'yellow'

def _select_row(o, r):
    logging.debug('Selecting row at index '+str(r)+'..')

    for i, row_eles in enumerate(o['ele']):
        bg_col = col_bg_row_deselected
        if i==r:
            bg_col = col_bg_row_selected

        for col_ele in row_eles:
             col_ele.configure(background=bg_col)

def _select_wo_call(o, i, r):
    _select_row(o, r)
    o['sel_id'] = i

def _select_if_not(o, i, r):
    if i!=o['sel_id']:
        _select_wo_call(o, i, r)
        if callable(o['on_select']):
            o['on_select'](i)

def _on_click_row(o, i, r, e):
    logging.debug('ID of clicked row at index '+str(r)+' is "'+i+'"."')

    _select_if_not(o, i, r)

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
        if k==o['sel_id']:
            sel_row = row # It would be possible to do without this..
        row = row+1
        
    _select_wo_call(o, o['sel_id'], sel_row)

    ttk.Style().configure('MT.TFrame', background=col_bg_table)
    o['frame'].configure(style='MT.TFrame')

    return o
