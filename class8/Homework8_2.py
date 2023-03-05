
import PIL.Image
import PIL.ImageTk

from tkinter import *

from tkinter import messagebox

root = Tk()

num = 0

root.title("Class7")

root.geometry("300x200+150+200")
img =PIL.Image.open("C:/Users/Lucas/Documents/Python_2022Autumn/class8/sofa.jpg")


tk_img = PIL.ImageTk.PhotoImage(img)

resized_image = img.resize((150, 100))

tk_img = PIL.ImageTk.PhotoImage(resized_image)

label = Label(root, image = tk_img)
label.grid(sticky = "W", row = 1, column = 0)
def add():
    global num
    numlabel["text"] = int(numlabel["text"])+1

def subtract():
    global num
    if int(numlabel["text"]) >0:
        numlabel["text"] = int(numlabel["text"])-1
    elif int(numlabel["text"]) ==0:
        messagebox.showinfo("showinfo", "The number of products can't be below 0.")
        numlabel["text"] = int(numlabel["text"])+1

a=Label(root, text = "Kube shop", font = ("Courier", 12, "bold"))
a.grid(row = 0, column = 0, columnspan = 3, sticky=W+E+N+S)

mybutton1 = Button(root, text = "-",  command = subtract)
mybutton2 = Button(root, text = "+",  command = add)

mybutton1.grid(row = 3, column = 1)
mybutton2.grid(row = 3, column = 3)
numlabel = Label(root, text = 0, font = ("Courier", 12, "bold"))
numlabel.grid(row = 3, column = 2, sticky = "W")
Label(root, text = "沙發組", font = ("Courier", 12, "bold")).grid(row = 2, column = 0, sticky = "W")
Label(root, text = "$1200", font = ("Courier", 12, "bold")).grid(row = 2, column = 1)
root.mainloop()
