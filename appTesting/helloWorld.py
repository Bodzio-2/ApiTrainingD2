from tkinter import *
from tkinter import ttk




root = Tk()
root.title('Simple Destiny Item Manager')

window_width = 300
window_height = 200

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

frm = ttk.Frame(root, padding=100)
frm.grid()



ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Add Text!", command=lambda: print("wtf")).grid(column=1, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=0)
ttk.Label(frm, text="You dumbass!").grid(column=0, row=1)
root.mainloop()


