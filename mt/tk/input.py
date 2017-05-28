
import tkinter as ti
from tkinter import ttk

border_title = 5
pad_entry = 5
pad_but = 5
pad_input = 5
col_bg_input = 'green'
but_text = 'Apply'

def _add_row(f, i, title, r):
    ret_val = {
        'var': ti.StringVar(),
        'ele': None # See below.
    }

    label = ttk.Label(f, text=title+':', border=border_title)
    label.grid(column=0, row=r, sticky=(ti.N, ti.S, ti.W, ti.E))
    label.configure(font='bold')

    # TODO: Add more than string input.
    #
    ret_val['ele'] = ttk.Entry(f, textvariable=ret_val['var'])
    ret_val['ele'].grid(
        column=1,
        row=r,
        padx=pad_entry,
        pady=pad_entry,
        sticky=(ti.N, ti.S, ti.W, ti.E))

    return ret_val

def _add_rows(f, id_to_titles):
    ret_val = {}
    r = 0

    for i, title in id_to_titles.items():
        ret_val[i] = _add_row(f, i, title, r)
        r = r+1

    return ret_val

def _add_but(f, r, on_click):
    ret_val = ttk.Button(f, text=but_text, command=on_click)

    ret_val.grid(
        column=0,
        row=r,
        padx=pad_but,
        pady=pad_but,
        sticky=(ti.N, ti.S, ti.W, ti.E))

    return ret_val

def set_enabled(o, is_enabled):
    state = ti.DISABLED
    if is_enabled:
        state = ti.NORMAL

    for k, v in o['var_and_eles'].items():
        v['ele'].configure(state=state)

    o['but'].configure(state=state)

def create(p):
    o = {
        'frame': ttk.Frame(p['frame']),
        'id': '',
        'var_and_eles': None, # See below.
        'but': None # See below.
    }

    o['frame'].grid(
        column=0,
        row=0,
        padx=pad_input,
        pady=pad_input,
        sticky=(ti.N, ti.S, ti.W, ti.E))

    o['var_and_eles'] = _add_rows(o['frame'], p['id_to_titles'])

    o['but'] = _add_but(
        o['frame'],
        len(p['id_to_titles']),
        lambda o=o: p['on_apply'](o))

    ttk.Style().configure('MTinput.TFrame', background=col_bg_input)
    o['frame'].configure(style='MTinput.TFrame')

    set_enabled(o, False)

    return o
