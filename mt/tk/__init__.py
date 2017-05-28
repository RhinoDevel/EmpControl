
def clear_frame(f):
    for widget in f.winfo_children():
        widget.destroy()
