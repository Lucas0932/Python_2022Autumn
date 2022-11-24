from tkinter import *
root = Tk()

root.geometry("200x100")

num = 0

root.title("Class6")

Label(root, text = "Kube shop", fg = "black", font = ("Courier", 12, "bold")).grid(row =  0, column = 0, columnspan = 4)
Label(root, text = "戶外餐桌椅組", fg = "black", font = ("Courier", 12, "bold")).grid(row =  1, column = 0, columnspan = 4, sticky = W)
Label(root, text = "$1200", fg = "black", font = ("Courier", 12, "bold")).grid(row =  2, column = 0, sticky = W)

def add():
    global num
    num+=1
    Label(root, text = num, font = ("Courier", 12, "bold")).grid()

def subtract():
    global num
    num-=1
    Label(root, text = num, font = ("Courier", 18, "bold")).grid()

mybutton1 = Button(root, text = "+",  command = add, width = 5).grid(row =  3, column = 0, sticky = W)
Label(root, text = num, fg = "black", font = ("Courier", 12, "bold")).grid(row =  3, column = 1, sticky = W+E)
mybutton2 = Button(root, text = "-",  command = subtract, width = 5).grid(row =  3, column = 2)

root.mainloop()