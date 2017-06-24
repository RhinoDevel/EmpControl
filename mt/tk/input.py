
import tkinter as ti
from tkinter import ttk

import mt.str

border_title = 5
pad_ele = 5
pad_but = 5
pad_input = 5
col_bg_input = 'green'
but_text = 'Apply'

def _combobox_on_selected(e, o):
    index = o['ele'].current()
    if index==-1:
        o['var'].set('')
    else:
        o['var'].set(o['values'][index])

def _combobox_get_index(i, o):
    if not mt.str.is_nonwhitespace(i):
        return 0#-1

    val = o['get_val_from_id'](i)

    return o['values'].index(val)

def _combobox_set(i, o):
    cur_index = o['ele'].current()
    index = _combobox_get_index(i, o)
    if cur_index==index:
        return
    o['ele'].current(index)
    _combobox_on_selected(None, o)

def _combobox_clear(o):
    _combobox_set('', o)

def _str_set(val, o):
    o['var'].set(val)

def _str_clear(o):
    _str_set('', o)

def _add_row(f, i, data, r):
    ret_val = {
        'var': None, # See below.
        'ele': None # See below.
    }

    label = ttk.Label(
        f, text=data['title']+':', border=border_title)
    label.grid(column=0, row=r, sticky=(ti.N, ti.S, ti.W, ti.E))
    label.configure(font='bold')

    if data['type']=='str':
        ret_val['var'] = ti.StringVar()
        ret_val['ele'] = ttk.Entry(f, textvariable=ret_val['var'])
        ret_val['set'] = lambda i, v, o=ret_val: _str_set(v, o)
        ret_val['clear'] = lambda o=ret_val: _str_clear(o)
    elif data['type']=='sel':
        ret_val['values'] = data['values']
        ret_val['var'] = ti.StringVar()
        ret_val['ele'] = ttk.Combobox(
            f,
            values=data['titles'],
            state='readonly')
        ret_val['set'] = lambda i, v, o=ret_val: _combobox_set(i, o)
        ret_val['clear'] = lambda o=ret_val: _combobox_clear(o)
        ret_val['get_val_from_id'] = data['get_val_from_id']

        ret_val['ele'].bind(
            '<<ComboboxSelected>>',
            lambda e, o=ret_val: _combobox_on_selected(e, o))
    #
    # Otherwise: Error!

    ret_val['ele'].grid(
        column=1,
        row=r,
        padx=pad_ele,
        pady=pad_ele,
        sticky=(ti.N, ti.S, ti.W, ti.E))

    return ret_val

def _add_rows(f, id_to_data):
    ret_val = {}
    r = 0

    for i, data in id_to_data.items():
        ret_val[i] = _add_row(f, i, data, r)
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
    """Create input element.

    p: # Dictionary.
        frame # To be filled.
        id_to_data # Ordered dictionary of dictionaries.
        on_apply # Function.
    """
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

    o['var_and_eles'] = _add_rows(o['frame'], p['id_to_data'])

    o['but'] = _add_but(
        o['frame'],
        len(p['id_to_data']),
        lambda o=o: p['on_apply'](o))

    ttk.Style().configure('MTinput.TFrame', background=col_bg_input)
    o['frame'].configure(style='MTinput.TFrame')

    return o
