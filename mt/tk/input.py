
import tkinter as ti
from tkinter import ttk

border_title = 5
pad_input = 5
col_bg_input = 'green'

def _add_row(f, t, r):
    label = ttk.Label(f, text=t+':', border=border_title)
    label.grid(column=0, row=r, sticky=(ti.N, ti.S, ti.W, ti.E))
    label.configure(font='bold')

    # TODO: Add user modifiable input/select element.

def _add_rows(f, titles):
    r = 0
    for t in titles:
        _add_row(f, t, r)
        r = r+1

def create(p):
    o = {
        'frame': ttk.Frame(p['frame'])
    }

    o['frame'].grid(
        column=0,
        row=0,
        padx=pad_input,
        pady=pad_input,
        sticky=(ti.N, ti.S, ti.W, ti.E))

    _add_rows(o['frame'], p['titles'])

    # TODO: Add apply button.

    ttk.Style().configure('MTinput.TFrame', background=col_bg_input)
    o['frame'].configure(style='MTinput.TFrame')

    return o
