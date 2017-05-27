
import tkinter as ti
from tkinter import ttk
import collections

import mt.tk.table

def menu():
    root = None
    mainframe = None
    nb = None
    nb_company = None
    nb_clients = None
    nb_workers = None
    nb_tasktypes = None
    nb_workdays = None
    nb_tasks = None

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
    nb_clients = ttk.Frame(nb)
    nb.add(nb_clients, text='Clients')
    nb_workers = ttk.Frame(nb)
    nb.add(nb_workers, text='Workers')
    nb_tasktypes = ttk.Frame(nb)
    nb.add(nb_tasktypes, text='Task Types')
    nb_workdays = ttk.Frame(nb)
    nb.add(nb_workdays, text='Workdays')
    nb_tasks = ttk.Frame(nb)
    nb.add(nb_tasks, text='Tasks')

    nb_company.columnconfigure(0, weight=1)
    nb_company.rowconfigure(0, weight=1)
    mt.tk.table.create({
            'frame': nb_company,
            'titles': ['Company ID', 'Title'],
            'entries': [
                ['12345678', 'Beerbarrèltree Brothers'],
                ['23456789', 'Mästermind Ltd.'],
                ['34567890', 'Fish-For-Br€akfast']],
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
