#創立類別
class Cars: #創立汽車類別
    #建構式
    def __init__(self, color, seat):
        self.color = color #顏色屬性
        self.seat = seat #座位屬性
    #方法
    def move(self, meter):
        print("Mr car moves", str(meter), "meters.")
    def printAttritbute(self):
        print("My car's color is", (self.color))
        print("My car has", str(self.seat), "seats.")
audi = Cars("blue", 4)
audi.move(5) #呼叫方法
audi.printAttritbute() #呼叫方法
class Motorcycle: #創立摩托車類別
    pass

# #創立物件
# audi = Cars() #創立Cars類別的物件

# #建立屬性
# audi.color = "blue" #顏色屬性
# audi.seat = 4 #座位屬性

# #呼叫屬性的值
# print(audi.color) #執行結果:blue
# print(audi.seat) #執行結果:4   

# #判斷類別跟物件之間的關係
# print(isinstance(audi, Cars)) #執行結果:True
# print(isinstance(audi, Motorcycle)) #執行結果:False

class FullName:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def PrintMyName(self):
        print("My name is", (self.firstname), (self.lastname))
name1 = FullName("Andy", "Wang")
name2 = FullName("Lulu", "Cheng")
name1.PrintMyName()
name2.PrintMyName()
print(name1.firstname, name1.lastname)
print(name2.firstname, name2.lastname)