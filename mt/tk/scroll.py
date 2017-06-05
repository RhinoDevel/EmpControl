
from tkinter import ttk
import tkinter as ti

def _on_frame_conf(canvas):
    canvas.configure(scrollregion=canvas.bbox('all'))

def get_vertical_scrollbar_frame(frame):
    canvas = ti.Canvas(frame, highlightthickness=0)
    inner = ttk.Frame(canvas)
    v_scrollbar = ti.Scrollbar(frame, orient='vertical', command=canvas.yview)

    canvas.configure(yscrollcommand=v_scrollbar.set)

    v_scrollbar.pack(side='right', fill='y')
    canvas.pack(side='left', fill='both', expand=True)

    canvas.create_window((0, 0), window=inner, anchor=ti.N+ti.W)
    frame.bind('<Configure>', lambda e, canvas=canvas: _on_frame_conf(canvas))

    return inner
