#引入 Pillow module
import PIL.Image
import PIL.ImageTk
# 引入 tkinter module
from tkinter import *
# 引入 tkinter 的 messagebox
from tkinter import messagebox
#建立主視窗 Frame
root = Tk()
#設定視窗標題
root.title("Class7")
#設定視窗大小
root.geometry("300x300+150+200")
# #更改label文字內容-way2
# #建立變數
# num = 0
# def clicked():
#     global num
#     num+=1
#     mystringvar.set("click" + str(num))

# #建立StringVar
# mystringvar = StringVar()
# mystringvar.set("click 0")
# #建立 計算按鈕次數 label 標籤
# mybutton = Button(root, textvariable = mystringvar, command = clicked)

# mybutton.pack()
# #執行主程式
# root.mainloop()
#----------------------------------------------------------------------
# #獲取label文字內容-way1
# #建立變數
# num = 0
# def clicked():
#     global num
#     num+=1
#     mylabel["text"] = ("click" + str(num))
# #建立計算按鈕次數 label 標籤
# mylabel = Button(root, text = "click 0", command = clicked)
# mylabel.pack()
# #執行主程式
# root.mainloop()
#----------------------------------------------------------------------
# #獲取label文字內容-way1
# #建立 計算按鈕次數 label 標籤
# mylabel = Button(root, text = "Hello World")
# mylabel.pack()
# #get mylabel的文字內容
# Label(root, text = mylabel["text"]).pack()
# #執行主程式
# root.mainloop()
# ----------------------------------------------------------------------
# #獲取label文字內容-way2
# #建立StringVar
# mystringvar = StringVar()
# mystringvar.set("Hello World!")
# #建立 計算按鈕次數 label 標籤
# mylabel = Button(root, textvariable = mystringvar)
# mylabel.pack()
# #get mylabel的文字內容
# Label(root, text = mystringvar.get()).pack()
# #執行主程式
# root.mainloop()
#----------------------------------------------------------------------
# #開啟圖片
# img =PIL.Image.open("C:/Users/Lucas/Documents/Python_2022Autumn/class8/corgi1.jpg")

# #轉換為 tk 圖片物件
# tk_img = PIL.ImageTk.PhotoImage(img)
# #更改圖片大小
# resized_image = img.resize((100, 100))
# ##轉換為 tk 圖片物件
# tk_img = PIL.ImageTk.PhotoImage(resized_image)
# #在 Lable 中放入圖片
# label = Label(root, image = tk_img)
# label.pack()
# #在 Button 中放入圖片
# Button = Button(root, image = tk_img)
# Button.pack()
# root.mainloop()
# #----------------------------------------------------------------------
#出現"message test"的普通訊息框
messagebox.showinfo("showinfo", "message test")
#出現提問訊息框
result = messagebox.askquestion("askquestion", "Is it Sunday?")
print("User click " + result)
#----------------------------------------------------------------------