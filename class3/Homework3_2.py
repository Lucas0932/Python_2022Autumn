class Minecraft:
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def eee(self):
        print("This location is at", str(self.x), ",", str(self.y), ",", str(self.z))
Home = Minecraft(-156, 63, 234)
Mining_Area = Minecraft(-156, -59, 406)
Home.eee()
Mining_Area.eee()