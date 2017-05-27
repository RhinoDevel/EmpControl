
import tkinter as ti
from tkinter import ttk

def _add_cell(frame, col, row, text, is_title):
    label = ttk.Label(frame, text=text, background='red')
    if is_title:
        label.configure(font='bold')
    label.grid(column=col, row=row, padx=5, pady=5, sticky=(ti.N, ti.W))

def _add_row(frame, row, texts, are_titles):
    col = 0
    for text in texts:
        _add_cell(frame, col, row, text, are_titles)
        col = col+1

def create(p):
    gui_style = ttk.Style()
    gui_style.configure('My.TButton', foreground='#334353')
    gui_style.configure('My.TFrame', background='#334353')

    frame = ttk.Frame(p['frame'], style='My.TFrame')
    frame.grid(column=0, row=0, padx=5, pady=5, sticky=(ti.N, ti.S, ti.W, ti.E))

    row = 0

    _add_row(frame, row, p['titles'], True)
    row = row+1

    for texts in p['entries']:
        _add_row(frame, row, texts, False)
        row = row+1

    return frame
