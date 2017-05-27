
import logging
import collections
import tkinter as ti
from tkinter import ttk

import mt.tk.table

def _on_select(i):
    logging.debug('Table entry with ID "'+i+'" was selected.')

def menu():
    root = None
    mainframe = None
    nb = None
    nb_company = None
    nb_client = None
    nb_worker = None
    nb_tasktype = None
    nb_workday = None
    nb_task = None

    root = ti.Tk()
    root.title('EmpControl')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(ti.N, ti.S, ti.W, ti.E))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    nb = ttk.Notebook(mainframe)
    nb.grid(column=0, row=0, padx=5, pady=5, sticky=(ti.N, ti.S, ti.W, ti.E))

    nb_company = ttk.Frame(nb)
    nb.add(nb_company, text='Companies')
    nb_client = ttk.Frame(nb)
    nb.add(nb_client, text='Clients')
    nb_worker = ttk.Frame(nb)
    nb.add(nb_worker, text='Workers')
    nb_tasktype = ttk.Frame(nb)
    nb.add(nb_tasktype, text='Task Types')
    nb_workday = ttk.Frame(nb)
    nb.add(nb_workday, text='Workdays')
    nb_task = ttk.Frame(nb)
    nb.add(nb_task, text='Tasks')

    nb_worker.columnconfigure(0, weight=1)
    nb_worker.rowconfigure(0, weight=1)
    mt.tk.table.create({
            'on_select': _on_select,#None,
            'frame': nb_worker,
            'sel_id': '34567890',#'',
            'titles': ['Lastname', 'Firstname'],
            'entries': collections.OrderedDict([
                ('12345678', [ 'Müller', 'Hans-Werner' ]),
                ('23456789', [ 'Niemandt', 'Agnés' ]),
                ('34567890', [ 'Steinkopf', 'Svenjä' ])])
        })

    root.mainloop()

#import tkinter.scrolledtext as st
#import logging
# apply_but = None
# desc_lab = None
# desc_inp = None
# vac_lab = None
# vac_chk = None
# vac_val = None
#
# def on_apply():
#     desc = desc_inp.get('1.0', ti.END+'-1c')
#     logging.debug('Description entered: "'+desc+'"')
#     logging.debug('Vacation: '+str(vac_val.get()))
#
# # Column 0 has fixed width.
# mainframe.columnconfigure(1, weight=1)
# mainframe.rowconfigure(0, weight=1)
#
# apply_but = ttk.Button(mainframe, text='Apply', command=on_apply)
# apply_but.grid(column=0, row=2, padx=5, pady=5, sticky=(ti.N, ti.W))
#
# desc_lab = ttk.Label(mainframe, text='Description'+':')
# desc_lab.grid(column = 0, row=0, padx=5, pady=5, sticky=(ti.N, ti.W))
# desc_inp = st.ScrolledText(mainframe, width=80, height=5, wrap=ti.WORD)
# desc_inp.grid(column = 1, row=0, padx=5, pady=5, sticky=(ti.N, ti.S, ti.W, ti.E))
#
# vac_lab = ttk.Label(mainframe, text='Vacation'+':')
# vac_lab.grid(column = 0, row=1, padx=5, pady=5, sticky=(ti.N, ti.W))
# vac_val = ti.BooleanVar()
# vac_val.set(False)
# vac_chk = ttk.Checkbutton(
#     mainframe,
#     variable=vac_val,
#     onvalue=True,
#     offvalue=False)
# vac_chk.grid(column = 1, row=1, padx=5, pady=5, sticky=(ti.N, ti.W))
#
#.focus()
