
import tkinter

num = 0
root = tkinter.Tk()

root.title("Class4_HW1")

root.geometry("225x75+150+200")

tkinter.Label(root, text = "三人座沙發 綠色/灰色/黑色", font = ("Courier", 12, "bold")).pack()

def add():
    global num
    num+=1
    tkinter.Label(root, text = num, font = ("Courier", 12, "bold")).pack(side = "right")

def subtract():
    global num
    num-=1
    tkinter.Label(root, text = num, font = ("Courier", 18, "bold")).pack(side = "right")

mybutton1 = tkinter.Button(root, text = "-",  command = subtract)
mybutton2 = tkinter.Button(root, text = "+",  command = add)

mybutton2.pack(side = "right")
tkinter.Label(root, text = num, font = ("Courier", 12, "bold")).pack(side = "right")
tkinter.Label(root, text = "NT.28,900", font = ("Courier", 12, "bold")).pack(side = "left")
mybutton1.pack(side = "right")

root.mainloop()