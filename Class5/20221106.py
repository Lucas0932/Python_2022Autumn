# 引入 tkinter module
from tkinter import *
#建立主視窗 Frame
root = Tk()
#設定視窗標題
root.title("Hi")
#設定視窗大小及彈出位置
root.geometry("300x300+150+200")
# #side: 排列方向: top(預設), bottom, left, right
# #fill: 填滿所分配空間之方向: NONE(預設), x, y, both
# #expand: 填滿容器: True/False(預設)
# #padx/ pady: 元件邊框與容器之距離(px, 預設 = 0)
# #ipadx/ ipady:  元件內容(文字/圖像)與其邊框之距離(px, 預設 = 0)
# #建立 label 標籤
mybutton1 = Button(root, text = "button1")
mybutton2 = Button(root, text = "button2")
mybutton3 = Button(root, text = "button3")
mybutton4 = Button(root, text = "button4")
mybutton5 = Button(root, text = "button5")
# #加入視窗中
# mybutton1.pack(side = "left")
# mybutton2.pack(side = "right")
# mybutton3.pack(side = "right")
# #加入視窗中
# mybutton1.pack(fill = "x")
# mybutton2.pack(side = "right", fill = "y")
# #加入視窗中
# mybutton1 = Button(root, text = "expand = 0")
# mybutton1.pack(fill = "both", expand = 0)
# mybutton2= Button(root, text = "expand = 1")
# mybutton2.pack(fill = "both", expand = 1)
# #加入視窗中
# mybutton1.pack(side = "left", padx = 20)
# mybutton2.pack(side = "right", padx = 30)
# #加入視窗中
# mybutton1.pack(side = "left", ipadx = 30)
# mybutton2.pack(side = "right", ipady = 30)
# #加入視窗中
mybutton1.pack(fill = "x")
mybutton2.pack(side = "left", fill = "y")
mybutton3.pack(side = "left")
mybutton4.pack(side = "right")
mybutton5.pack(side = "top")
#執行主程式
root.mainloop()