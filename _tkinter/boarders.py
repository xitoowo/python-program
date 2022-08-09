import tkinter


boarders = {
    "flat": tkinter.FLAT,
    "sunken": tkinter.SUNKEN,
    "raised": tkinter.RAISED,
    "groove": tkinter.GROOVE,
    "ridge": tkinter.RIDGE
}

window = tkinter.Tk()

for relief_name, relief in boarders.items():
    frame = tkinter.Frame(master=window, relief=relief, borderwidth=5)
    frame.pack(side=tkinter.LEFT)
    lbl = tkinter.Label(master=frame, text=relief_name)
    lbl.pack()

window.mainloop()