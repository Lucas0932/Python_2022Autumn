from tkinter import *
from datetime import *

root =Tk()

root.title("Class4_HW2")

root.geometry("400x400+150+200")

Label(root, text = "Enter your Birthday:\nInput format is yyyy.mm.dd", fg = "black", font = ("Arial", 18, "bold")).pack()

e = Entry(root, width = 30, font = ("Arial", 18, "bold"))

e.pack()

def count():
    time_string = e.get()
    t1 = datetime.strptime(time_string,"%Y.%m.%d")
    t2 = datetime.now()
    result = t2.year-t1.year
    label = Label(root, text = "You are "+ str(result)+ " years old.")
    label.pack()

Button1 = Button(root, text = "Enter!", command = count, font = ("Arial", 18, "bold"))
Button1.pack(pady = 20)
root.mainloop()