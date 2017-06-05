
import logging
from enum import Enum
import tkinter as ti
from tkinter import ttk

import mt.tk.label

class CellType(Enum):
    title = 1
    delete = 2
    text = 3

cell_text_avg_char_width = 16 # In average character width.
cell_but_avg_char_width = 1 # In average character width.
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

def _on_delete(o, i):
    logging.debug('On-delete function called for ID "'+i+'".')

    o['on_delete'](i)

def _on_click_row(o, i, r, e):
    logging.debug('ID of clicked row at index '+str(r)+' is "'+i+'"."')

    _select_toggle(o, i, r)

def _add_cell(o, col, row, i, text, cell_type):
    is_title = cell_type==CellType.title
    is_text = cell_type==CellType.text
    ele = None
    width = -1
    frame = o['frame_title'] if is_title else o['frame_data']

    if is_title or is_text:
        width = cell_text_avg_char_width
        if is_title and col==0: # Delete button.
            width = cell_but_avg_char_width

        ele = ttk.Label(
            frame,
            text=text,
            border=border_cell,
            width=width)
    else: # Assuming CellType.delete.
        width = cell_but_avg_char_width
        ele = ti.Frame(frame)
        #ele.columnconfigure(0, weight=1)
        #ele.rowconfigure(0, weight=1)
        but = ttk.Button(
            ele,
            text='d', # TODO: Replace with icon.
            width=width,
            command=lambda i=i, o=o: _on_delete(o, i))
        but.grid(column=0, row=0)

    ele.grid(column=col, row=row, sticky=(ti.N, ti.S, ti.W, ti.E))

    if is_text:
        ele.bind(
            "<Button-1>", lambda e, i=i, o=o, r=row: _on_click_row(o, i, r, e))
        ele.update() # For next function to work.
        ele['text'] = mt.tk.label.get_ellipsis_text(ele, ele['text'])

    ele.configure(background=col_bg_row_deselected)

    o['ele'][row].append(ele)

def _add_row(o, row, i, texts, are_titles):
    col = 0
    o['ele'].append([])

    if callable(o['on_delete']):
        if are_titles:
            _add_cell(o, col, row, i, '', CellType.title)
        else:
            _add_cell(o, col, row, i, None, CellType.delete)
        col = col+1

    for text in texts:
        _add_cell(
            o,
            col,
            row,
            i,
            text,
            CellType.title if are_titles else CellType.text)
        col = col+1

def create(p):
    o = {
        'frame': ttk.Frame(p['frame']),
        'frame_title': None, # See below.
        'frame_data': None, # See below.
        'on_deselect': p['on_deselect'],
        'on_select': p['on_select'],
        'on_delete': p['on_delete'],
        'ele': [],
        'sel_id': p['sel_id']
    }
    o['frame_title'] = ttk.Frame(o['frame'])
    o['frame_data'] = ttk.Frame(o['frame'])

    o['frame'].grid(
        column=0,
        row=0,
        padx=pad_table,
        pady=pad_table,
        sticky=(ti.N, ti.S, ti.W, ti.E))
    o['frame_title'].grid(
        column=0,
        row=0,
        padx=0,
        pady=0,
        sticky=(ti.N, ti.S, ti.W, ti.E))
    o['frame_data'].grid(
        column=0,
        row=1,
        padx=0,
        pady=0,
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
