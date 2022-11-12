from tkinter import *
root = Tk()
root.title("Hi")
root.geometry("300x300+150+200")

mybutton1 = Button(root, text = "button1")
mybutton2 = Button(root, text = "button2")
mybutton3 = Button(root, text = "button3")
mybutton4 = Button(root, text = "button4")
mybutton5 = Button(root, text = "button5")

mybutton1.pack(fill = "x")
mybutton2.pack(side = "left", fill = "y")
mybutton3.pack(side = "left")
mybutton4.pack(side = "right")
mybutton5.pack(side = "top")

root.mainloop()