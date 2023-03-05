#引入 Pillow module
import PIL.Image
import PIL.ImageTk
# 引入 tkinter module
from tkinter import *
# 引入 tkinter 的 messagebox
from tkinter import messagebox
#------------------------------------------------------------------------
# #建立主視窗 Frame
# root = Tk()
# #設定視窗標題
# root.title("Class9")
# #設定視窗大小
# root.geometry("300x300+150+200")
# #執行主程式
# root.mainloop()
#------------------------------------------------------------------------
# #建立主視窗  Frame
# root = Tk()
# #放入第一個單選按鈕
# radiobtn1 = Radiobutton(root, text = "Black")
# radiobtn1.pack()
# #放入第二個單選按鈕
# radiobtn2 = Radiobutton(root, text = "Red")
# radiobtn2.pack()
# #執行主程式
# root.mainloop()
#------------------------------------------------------------------------
# #建立主視窗  Frame
# root = Tk()
# #宣告一個文字變數
# val = StringVar()
# #放入第一個單選按鈕
# radiobtn1 = Radiobutton(root, text = "Black", variable = val, value = "Black")
# radiobtn1.pack()
# #指定選取第一個單選按鈕
# radiobtn1.select()
# #放入第二個單選按鈕
# radiobtn2 = Radiobutton(root, text = "Red", variable = val, value = "Red")
# radiobtn2.pack()
# #執行主程式
# root.mainloop()
#------------------------------------------------------------------------
# #建立主視窗  Frame
# root = Tk()
# #建立問題
# question = Label(root, text = "Please select the color you prefer")
# question.pack()
# #宣告一個文字變數
# val = StringVar()
# #放入第一個單選按鈕
# radiobtn1 = Radiobutton(root, text = "Blue", variable = val, value = "Blue", fg = "Blue")
# radiobtn1.pack()
# #放入第二個單選按鈕
# radiobtn2 = Radiobutton(root, text = "Green", variable = val, value = "green", fg = "Green")
# radiobtn2.pack()
# #指定選取第二個單選按鈕
# radiobtn2.select()
# #放入第三個單選按鈕
# radiobtn3 = Radiobutton(root, text = "Pink", variable = val, value = "Pink", fg = "Pink")
# radiobtn3.pack()
# #執行主程式
# root.mainloop()
#------------------------------------------------------------------------
# #建立主視窗  Frame
# root = Tk()
# #建立問題
# question = Label(root, text = "Please select the color you prefer")
# question.pack()
# #宣告一個文字變數
# val = StringVar()
# #label顏色依顏色內容更換
# def clicked1():
#     mylabel["fg"] = "Blue"
#     mylabel["textvariable"] = val
# def clicked2():
#     mylabel["fg"] = "Green"
#     mylabel["textvariable"] = val
# def clicked3():
#     mylabel["fg"] = "Pink"
#     mylabel["textvariable"] = val
# #放入第一個單選按鈕
# radiobtn1 = Radiobutton(root, text = "Blue", variable = val, value = "Blue", fg = "Blue", command = clicked1)
# radiobtn1.pack()
# #放入第二個單選按鈕
# radiobtn2 = Radiobutton(root, text = "Green", variable = val, value = "green", fg = "Green", command = clicked2)
# radiobtn2.pack()
# #指定選取第二個單選按鈕
# radiobtn2.select()
# #放入第三個單選按鈕
# radiobtn3 = Radiobutton(root, text = "Pink", variable = val, value = "Pink", fg = "Pink", command = clicked3)
# radiobtn3.pack()
# #顯示被獲取按鈕之value
# mylabel = Label(root, textvariable = val, font = ("Arial", 30))
# mylabel.pack()
# #執行主程式
# root.mainloop()
#------------------------------------------------------------------------
# #建立主視窗  Frame
# root = Tk()
# #建立新視窗New Windows
# newWindow = Toplevel(root)
#------------------------------------------------------------------------
# #建立主視窗  Frame
# root = Tk()
# #點擊button跳出 New Windows
# def createNewWindow():
#     #建立新視窗New Windows
#     newWindow = Toplevel(root)
#     #建立新label在New Windows裡
#     mylabel = Label(newWindow, text = "New Window")
#     mylabel.pack
#     #建立新button在New Windows裡
#     mybutton = Button(newWindow, text = "New Window button")
#     mybutton.pack()
#     #執行新視窗城市
#     newWindow.mainloop()

# #點擊button產生NewWindows
# createnewwindowbtn = Button(root, text = "Click to Create New Windows!", command = createNewWindow)
# createnewwindowbtn.pack()
# #執行主程式
# root.mainloop()
#------------------------------------------------------------------------
# #建立主視窗  Frame
# root = Tk()
# #點擊button跳出 New Windows
# def createNewWindow():
#     #建立新視窗New Windows
#     newWindow = Toplevel(root)
#     #建立新label在New Windows裡
#     mylabel = Label(newWindow, text = "New Window")
#     mylabel.pack
#     #建立destroy button在New Windows裡
#     destroybutton = Button(newWindow, text = "Quit", command = newWindow.destroy)
#     destroybutton.pack()
#     #建立hide button在New Windows裡
#     hidebutton = Button(newWindow, text = "Hide", command = root.iconify)
#     hidebutton.pack()
#     #建立show button在New Windows裡
#     showbutton = Button(newWindow, text = "Show", command = root.deiconify)
#     showbutton.pack()
#     #建立withdraw button在New Windows裡
#     withdrawbutton = Button(newWindow, text = "Withdraw Main Window", command = root.withdraw )
#     withdrawbutton.pack()
#     #執行新視窗城市
#     newWindow.mainloop()

# #點擊button產生NewWindows
# createnewwindowbtn = Button(root, text = "Click to Create New Windows!", command = createNewWindow)
# createnewwindowbtn.pack()
# #執行主程式
# root.mainloop()
#------------------------------------------------------------------------
# def function(n, *args):
#     print(n)
#     print(args)
# #呼叫執行function，並給多個(>2個)三數值傳入該function
# #除了1為變數n外，及於都是*args的輸入值
# function(1,2,3,4,5,6,7)
#------------------------------------------------------------------------
# def function(*args, **kwargs):
#     print(kwargs)
#     print(args)
# #呼叫執行function，並給多個(>2個)三數值傳入該function
# #前四個值為*args可變參數，後兩個值為**kwargs關鍵字可變參數
# function(1,2,3,4, num1 = 5, num2 = 10)
#------------------------------------------------------------------------
# #建立主視窗  Frame
# root = Tk()
# def createNewWindow():
#     #建立新視窗New Windows
#     newWindow = Toplevel(root)
#     #建立問題
#     question = Label(newWindow, text = "Please select the color you prefer")
#     question.pack()
#     #宣告一個文字變數
#     val = StringVar()
#     #label顏色依顏色內容更換
#     def clicked1():
#         mylabel["fg"] = "Blue"
#         mylabel["textvariable"] = val
#     def clicked2():
#         mylabel["fg"] = "Green"
#         mylabel["textvariable"] = val
#     #放入第一個單選按鈕
#     radiobtn1 = Radiobutton(newWindow, text = "Blue", variable = val, value = "Blue", fg = "Blue", command = clicked1)
#     radiobtn1.pack()
#     #放入第二個單選按鈕
#     radiobtn2 = Radiobutton(newWindow, text = "Green", variable = val, value = "green", fg = "Green", command = clicked2)
#     radiobtn2.pack()
#     #指定選取第二個單選按鈕
#     radiobtn2.select()
#     #顯示被獲取按鈕之value
#     mylabel = Label(newWindow, textvariable = val, font = ("Arial", 30))
#     mylabel.pack()
#     #建立destroy button在New Windows裡
#     destroybutton = Button(newWindow, text = "Quit", command = newWindow.destroy)
#     destroybutton.pack()
# #點擊button產生NewWindows
# press_start = Button(root, text = "Start", command = createNewWindow)
# press_start.pack()
# #執行主程式
# root.mainloop()
#------------------------------------------------------------------------
def function(n, *args, **kwargs):
    print("有" + str(n) + "個數相加")
    a = 0
    for b in args:
        a = a+b
    for c in kwargs.values():
        a = a+c
    print("Sum = " + str(a))

function(6, 4, 3, 2, 1, n1 = 10, n2 = 20)
#------------------------------------------------------------------------