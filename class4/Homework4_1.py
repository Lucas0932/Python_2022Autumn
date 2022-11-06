
import tkinter

num = 0
root = tkinter.Tk()

root.title("Class4_HW1")

root.geometry("400x400+150+200")

tkinter.Label(root, text = "點擊按鈕次數計算", fg = "orange", font = ("Courier", 18, "bold")).pack()

def clicked():
    global num
    num+=1
    tkinter.Label(root, text = num, font = ("Courier", 18, "bold")).pack()

mybutton = tkinter.Button(root, text = "Click me!",  command = clicked)

mybutton.pack()

root.mainloop()