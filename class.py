class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def func(self):
        print("Fruit is " + self.name)

f1= Fruit("Banana", "Yellow")
print(f1.func())