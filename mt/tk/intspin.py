
import tkinter as ti
from tkinter import ttk

import mt.calc

def _get_nearest_valid(strval, from_, to):
    f = 0.0
    i = 0

    # A number must be entered:
    #
    try:
        f = float(strval)
    except ValueError:
        return from_ # Use first valid number.
    i = mt.calc.round(f) # Rounds floats.

    # Clip, if out of range:
    #
    if i < from_:
        return from_
    if i > to:
        return to

    return i

def _set_to_nearest_valid(strval, textvar, from_, to):
    textvar.set(_get_nearest_valid(strval, from_, to))

def _on_focus_out(event, textvar, from_, to):
    _set_to_nearest_valid(textvar.get(), textvar, from_, to)

def create(p):
    """Create integer number range input element.

    p: # Dictionary.
        frame # To be filled.
        pad # Padding to be used around input element.
        width
        from
        to
    """

    o = {
        'set': None, # See below.
        'get': None # See below.
    }
    textvar = ti.StringVar()
    s = ti.Spinbox(
        p['frame'],
        justify=ti.RIGHT,
        width=p['width'],
        wrap=True,
        textvariable=textvar,
        from_=p['from'],
        to=p['to'])
    s.bind(
        '<FocusOut>',
        lambda e, v = textvar, f = p['from'], t = p['to']:
            _on_focus_out(e, v, f, t))

    o['set'] = (lambda s, v = textvar, f = p['from'], t = p['to']:
        _set_to_nearest_valid(s, v, f, t))
    o['get'] = lambda: _get_nearest_valid(textvar.get(), p['from'], p['to'])

    p['frame'].columnconfigure(0, weight=1)
    p['frame'].rowconfigure(0, weight=1)
    s.grid(
        column=0,
        row=0,
        padx=p['pad'],
        pady=p['pad'],
        sticky=(ti.N, ti.S, ti.W, ti.E))

    return o
