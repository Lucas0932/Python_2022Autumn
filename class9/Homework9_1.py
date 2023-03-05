
import PIL.Image
import PIL.ImageTk

from tkinter import *

from tkinter import messagebox

root = Tk()

num = 1

root.title("Class7")

root.geometry("300x200+150+200")
img =PIL.Image.open("C:/Users/Lucas/Documents/Python_2022Autumn/class8/sofa.jpg")


tk_img = PIL.ImageTk.PhotoImage(img)

resized_image = img.resize((150, 100))

tk_img = PIL.ImageTk.PhotoImage(resized_image)

label = Label(root, image = tk_img)
label.grid(sticky = "W", row = 1, column = 0, rowspan = 3, columnspan = 2)
def add():
    if int(num["text"])>=5:
        newWindow = Toplevel(root)
        newWindow.geometry("200x100")
        warninglabel = Label(newWindow, text = "目前庫存最多只有5件")
        quitbutton = Button(newWindow, text = "Quit", command = newWindow.destory)
        newWindow.mainloop
    else:
        global num
        num+=1
        num["text"] = ((num))

def subtract():
    global num
    num-=1
    num["text"] = ((num))

a=Label(root, text = "Kube shop", font = ("Courier", 12, "bold"))
a.grid(row = 0, column = 0, columnspan = 4, sticky=W+E+N+S)

val = StringVar()

mybutton1 = Button(root, text = "-",  command = subtract)
mybutton2 = Button(root, text = "+",  command = add)
radiobtn1 = Radiobutton(root, text = "黑色", variable = val, value = "黑色")
radiobtn2 = Radiobutton(root, text = "灰色", variable = val, value = "灰色", state = DISABLED)
radiobtn3 = Radiobutton(root, text = "咖啡色", variable = val, value = "咖啡色")
selectlabel = Label(root, textvariable = val)

mybutton1.grid(row = 5, column = 1)
mybutton2.grid(row = 5, column = 3)
radiobtn1.grid(row = 1, column = 2, sticky = W+E+N+S)
radiobtn2.grid(row = 2, column = 2, sticky = W+E+N+S)
radiobtn3.grid(row = 3, column = 2, sticky = W+E+N+S)
Label(root, text = num, font = ("Courier", 12, "bold")).grid(row = 5, column = 2)
Label(root, text = "沙發組", font = ("Courier", 12, "bold")).grid(row = 4, column = 0)
Label(root, text = "$1200", font = ("Courier", 12, "bold")).grid(row = 4, column = 1)
root.mainloop()
