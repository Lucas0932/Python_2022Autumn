
from tkinter import *

root = Tk()

root.title("Class6")

mybutton1 = Button(root, text = "Result").grid(row = 0, column = 2, rowspan = 2, sticky = N + S)

def open(event = None):
    print("opened")
    menubar1.entryconfig("Execute", state = "normal")
def execute(event = None):
    print("Executed")
def exit(event = None):
    print("exited")
    
    menubar1.entryconfig("Execute", state = "disabled")

menu = Menu(root)

menubar1 = Menu(menu, tearoff = 0)

menubar1.add_command(label = "Open", command = open, accelerator = "Control+O", state = "normal")
menubar1.add_command(label = "Execute", command = execute, accelerator = "Control+S", state = "disabled")
menubar1.add_command(label = "Exit", command = exit, accelerator = "Control+E")

menubar1.add_separator()

menu.add_cascade(label = "File", menu = menubar1)

root.bind_all(open)
root.bind_all(execute)
root.bind_all(exit)

menubar2 = Menu(menu, tearoff = 0)

menubar2.add_command(label = "AAA")
menubar2.add_command(label = "BBB")

menubar2more = Menu(menubar2, tearoff = 0)
menubar2more.add_command(label = "X")
menubar2more.add_command(label = "Y")
menubar2.add_cascade(label = "Place", menu = menubar2)

menu.add_cascade(label = "Triple", menu = menubar2)

root.config(menu = menu)

root.mainloop()