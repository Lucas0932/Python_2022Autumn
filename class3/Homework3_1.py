class People:

    def __init__(self, height, weight, age):
        self.height = height
        self.weight = weight
        self.age = age
    def eee(self):
        print("I am", str(self.height), "cm,", str(self.weight), "kg,", str(self.age), "years old.")
dad = People(170, 70, 49)
mom = People(160, 45, 45)
Lucas = People(147, 39, 13)
dad.eee()
mom.eee()
Lucas.eee()