# 引入 tkinter module
import tkinter
#建立主視窗 Frame
root = tkinter.Tk()
#設定視窗標題
root.title("Hello World")
#設定視窗大小及彈出位置
root.geometry("600x400+150+200")
#將 label 加入視窗中
tkinter.Label(root, text = "Enter your name", fg = "black", font = ("Arial", 16, "bold")).pack()
#點擊按鈕函式function
def clicked():
    tkinter.Label(root, text = "Hi "+ e.get()+ "你好", font = ("Arial", 16, "bold")).pack()
#建立 Input Entry Boxes
e = tkinter.Entry(root, width = 20, font = ("Impact", 20))
e.pack()
#建立 button 按鈕
mybutton = tkinter.Button(root, text = "Enter", command = clicked)
#加入視窗中
mybutton.pack()
#執行主程式
root.mainloop()