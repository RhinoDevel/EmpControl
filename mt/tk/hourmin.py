
import tkinter as ti
from tkinter import ttk

import mt.tk.intspin

sep = ':'
width = 3

def _set(hourstr, minstr, hourset, minset):
    hourset(hourstr)
    minset(minstr)

def create(p):
    """Create hour & minutes input element.

    p: # Dictionary.
        frame # To be filled.
        pad # Padding to be used around hour & minutes input element.
    """

    frame = ttk.Frame(p['frame'])
    hourframe = None
    minframe = None
    hour = None
    min_ = None
    o = {
        'get': None, # See below.
        'set': None # See below.
    }

    p['frame'].columnconfigure(0, weight=1)
    p['frame'].rowconfigure(0, weight=1)
    frame.grid(
        column=0,
        row=0,
        padx=p['pad'],
        pady=p['pad'],
        sticky=(ti.N, ti.S, ti.W, ti.E))

    hourframe = ttk.Frame(frame)
    hour = mt.tk.intspin.create(
        {'frame': hourframe, 'pad': 0, 'width': width, 'from': 0, 'to': 23})
    hourframe.grid(column=0, row=0, sticky=(ti.N, ti.S, ti.W, ti.E))

    ttk.Label(frame, text=sep).grid(
        column=1, row=0, sticky=(ti.N, ti.S, ti.W, ti.E))

    minframe = ttk.Frame(frame)
    min_ = mt.tk.intspin.create(
        {'frame': minframe, 'pad': 0, 'width': 3, 'from': 0, 'to': 59})
    minframe.grid(column=2, row=0, sticky=(ti.N, ti.S, ti.W, ti.E))

    o['get'] = lambda: {'hour': hour['get'](), 'min': min_['get']()}
    o['set'] = (lambda hstr, mstr, hset = hour['set'], mset = min_['set']:
        _set(hstr, mstr, hset, mset))

    return o
