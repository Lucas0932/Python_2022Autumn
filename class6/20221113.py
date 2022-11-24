# #anchor: 元件在容器中的錨定位置: E, W, S, N, CENTER(預設), NE, SE, SW, NW
# #rowspan: 儲存格合併列數
# #columnspan: 儲存格合併行數
# #sticky: 元件於網格中的錨定位置: E, W, S, N, CENTER(預設)
# 引入 tkinter module
from tkinter import *
#建立主視窗 Frame
root = Tk()
#設定視窗標題
root.title("Class6")
#設定視窗大小及彈出位置
#root.geometry("350x100")
# #建立 label 標籤
mybutton1 = Button(root, text = "Result").grid(row = 0, column = 2, rowspan = 2, sticky = N + S)
# mybutton2 = Button(root, text = "2").grid(row = 0, column = 1)
# mybutton3 = Button(root, text = "3").grid(row = 0, column = 2)
# mybutton4 = Button(root, text = "4").grid(row = 1, column = 0, columnspan = 2, sticky = W + E)
# mybutton5 = Button(root, text = "5").grid(row = 1, column = 2)
# mybutton6 = Button(root, text = "6").grid(row = 2, column = 1)
#建立 Input Entry Boxes
Label(root, text = "Width", fg = "black", font = ("Courier", 12, "bold")).grid(row =  0, column = 0)
e = Entry(root, width = 20, font = ("Impact", 20))
e.grid(row = 0, column = 1)
Label(root, text = "Height", fg = "black", font = ("Courier", 12, "bold")).grid(row = 1, column = 0)
e1 = Entry(root, width = 20, font = ("Impact", 20))
e1.grid(row = 1, column = 1)
def open(event = None):
    print("opened")
    menubar1.entryconfig("Save", state = "normal")
def save(event = None):
    print("saved")
def exit(event = None):
    print("exited")
    # root.destroy()
    menubar1.entryconfig("Save", state = "disabled")
#建立主選單
menu = Menu(root)
#建立子選單，選單綁定 menubar 主選單
menubar1 = Menu(menu, tearoff = 0)
#子選單項目
menubar1.add_command(label = "Open", command = open, accelerator = "Control+O", state = "normal")
menubar1.add_command(label = "Save", command = save, accelerator = "Control+S", state = "disabled")
menubar1.add_command(label = "Exit", command = exit, accelerator = "Control+E")
#建立只選單，內容為子選單
menu.add_cascade(label = "File", menu = menubar1)
root.bind_all("<Control-o>", open)
root.bind_all("<Control-s>", save)
root.bind_all("<Control-e>", exit)
#建立第二個選單裡的子選單，有三個選項
menubar2 = Menu(menu, tearoff = 0)
#子選單項目
menubar2.add_command(label = "AAA")
menubar2.add_command(label = "BBB")
menubar2.add_command(label = "CCC")
#建立只選單，內容為子選單
menubar2.add_separator()
#建立子選單裡的子選單，有三個選項
menubar2more = Menu(menubar2, tearoff = 0)
menubar2more.add_command(label = "X")
menubar2more.add_command(label = "Y")
menubar2more.add_command(label = "Z")
menubar2.add_cascade(label = "File", menu = menubar2more)
#建立第二個選單 File，綁定子選單
menu.add_cascade(label = "Test", menu = menubar2)
#主視窗加入主選單
root.config(menu = menu)
#執行主程式
root.mainloop()