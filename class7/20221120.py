# 引入 tkinter module
from tkinter import *
#建立主視窗 Frame
root = Tk()
#設定視窗標題
root.title("Class7")
#設定視窗大小
root.geometry("300x300+150+200")
# #更改label文字內容-方法1
# #建立變數
# num = 0
# def clicked():
#     global num
#     num+=1
#     mystringvar.set("click" + str(num))

# mybutton = Button(root, text = "Click me!",  command = clicked)
# #建立StringVar
# mystringvar = StringVar()
# mystringvar.set("click 0")
# #建立 計算按鈕次數 label 標籤
# mylabel = Label(root, textvariable = mystringvar)
# Label(root, text = "點擊按鈕次數計算", fg = "orange", font = ("Courier", 18, "bold")).pack()

# mybutton.pack()
# mylabel.pack()
# #更改label文字內容-方法2
# num = 0
# def clicked():
#     global num
#     num+=1
#     mylabel["text"] = ("click" + str(num))

# mybutton = Button(root, text = "Click me!",  command = clicked)
# #建立 計算按鈕次數 label 標籤
# mylabel = Label(root, text = "click 0")

# Label(root, text = "點擊按鈕次數計算", fg = "orange", font = ("Courier", 18, "bold")).pack()

# mybutton.pack()
# mylabel.pack()
# #獲取label文字內容-way1
# #建立計算按鈕次數 label 標籤
# mylabel = Label(root, text = "Hello World")
# mylabel.pack()
# #get mylabel的文字內容
# Label(root, text = mylabel["text"]).pack()
#獲取label文字內容-way2
#建立StringVar
mystringvar = StringVar()
mystringvar.set("Hello World!")
#建立 計算按鈕次數 label 標籤
mylabel = Label(root, textvariable = mystringvar)
mylabel.pack()
#get mylabel的文字內容
Label(root, text = mystringvar.get()).pack()
# #Frame 元件
# frame1 = Frame(root, pady = 5, padx = 10, bg = "lightgreen")
# frame2 = Frame(root, pady = 10, padx = 2, bg = "lightblue")
# #放到 frame1 裡的 label
# label1 = Label(frame1, text = "First", width = 5)
# label1.pack()
# #放到 frame2 裡的 label
# label2 = Label(frame2, text = "Second", width = 10)
# label2.pack()
# #先放frame2
# frame2.pack(side = "right")
# #先放frame1
# frame1.pack(side = "left")

#執行主程式
root.mainloop()