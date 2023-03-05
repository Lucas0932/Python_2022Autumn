
import tkinter

num = 0
root = tkinter.Tk()

root.title("Class4_HW1")

root.geometry("225x75+150+200")


def add():
    global num
    num+=1
    tkinter.Label(root, text = num, font = ("Courier", 12, "bold")).grid()

def subtract():
    global num
    num-=1
    tkinter.Label(root, text = num, font = ("Courier", 18, "bold")).grid()

a=tkinter.Label(root, text = "Kube shop", font = ("Courier", 12, "bold"))
a.grid(row = 0, column = 0, columnspan = 4, sticky=W+E+N+S)

mybutton1 = tkinter.Button(root, text = "-",  command = subtract)
mybutton2 = tkinter.Button(root, text = "+",  command = add)

mybutton1.grid(row = 2, column = 1)
mybutton2.grid(row = 2, column = 3)
tkinter.Label(root, text = num, font = ("Courier", 12, "bold")).grid(row = 2, column = 2)
tkinter.Label(root, text = "沙發", font = ("Courier", 12, "bold")).grid(row = 1, column = 0)
tkinter.Label(root, text = "$1200", font = ("Courier", 12, "bold")).grid(row = 1, column = 1)

root.mainloop()