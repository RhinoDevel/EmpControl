
# Console-based (non-production) UI:
#
import ec.ui.console
#
ec.ui.console.menu()

# Playing around with Tk for GUI implementation:
#
# import logging
# import tkinter as ti
# import tkinter.scrolledtext as st
# from tkinter import ttk
#
# root = None
# mainframe = None
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
# logging.basicConfig(level=logging.DEBUG)
#
# root = ti.Tk()
# root.title('EmpControl')
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
#
# mainframe = ttk.Frame(root)
# mainframe.grid(column=0, row=0, sticky=(ti.N, ti.S, ti.W, ti.E))
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
# #.focus()
#
# root.mainloop()
