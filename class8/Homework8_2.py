
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
label.grid(sticky = "W", row = 1, column = 0)
def add():
    global num
    num+=1
    Label(root, text = num, font = ("Courier", 12, "bold")).grid()

def subtract():
    global num
    num-=1
    Label(root, text = num, font = ("Courier", 12, "bold")).grid()
    if num == 0:
        messagebox.showinfo("showinfo", "The number of products can't be below 0.")

a=Label(root, text = "Kube shop", font = ("Courier", 12, "bold"))
a.grid(row = 0, column = 0, columnspan = 4, sticky=W+E+N+S)

mybutton1 = Button(root, text = "-",  command = subtract)
mybutton2 = Button(root, text = "+",  command = add)

mybutton1.grid(row = 3, column = 1)
mybutton2.grid(row = 3, column = 3)
Label(root, text = num, font = ("Courier", 12, "bold")).grid(row = 3, column = 2)
Label(root, text = "沙發組", font = ("Courier", 12, "bold")).grid(row = 2, column = 0)
Label(root, text = "$1200", font = ("Courier", 12, "bold")).grid(row = 2, column = 1)
root.mainloop()
