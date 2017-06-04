
import tkinter as ti
from tkinter import ttk
from tkinter import font

fontname_default = 'TkDefaultFont'
ellipsis = '...'
ellipsis_len = len(ellipsis)

def get_text_pix_len(label, text):
    font = None

    if label['font']:
        font = ti.font.Font(font=label['font'])
    else:
        font = ti.font.nametofont(fontname_default)

    return font.measure(text)

def get_ellipsis_text(label, text):
    buf = None
    borderlen = 2*label['border'] if label['border'] else 2 # Hard-coded 2.
    lablen = label.winfo_width()-borderlen
    index = -1

    if get_text_pix_len(label, text)<=lablen:
        return text

    buf = text+ellipsis

    while get_text_pix_len(label, buf)>lablen:
        index = len(buf)-ellipsis_len-1
        buf = buf[:index]+buf[index+1:]
        print(str(get_text_pix_len(label, buf))+' '+str(lablen)+' '+buf)
        if len(buf)<=ellipsis_len:
            return ellipsis

    return buf
