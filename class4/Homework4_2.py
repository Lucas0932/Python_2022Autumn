
import tkinter

root = tkinter.Tk()

root.title("Hello World")

root.geometry("600x400+150+200")

tkinter.Label(root, text = "Enter your name", fg = "black", font = ("Arial", 16, "bold")).pack()

def clicked():

    tkinter.Label(root, text = "Hi "+ e.get()+ "，你好。", font = ("Arial", 16, "bold")).pack()

e = tkinter.Entry(root, width = 20, font = ("Impact", 20))

e.pack()

mybutton = tkinter.Button(root, text = "Enter", command = clicked)

mybutton.pack()

root.mainloop()