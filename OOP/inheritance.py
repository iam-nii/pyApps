class Animal:
    def __init__(self):
        self.number_of_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")

class Fish(Animal):

    def __init__(self):
        super().__init__()

    def swim(self):
        print("moving in water")
    def breathe(self):
        super().breathe()
        print("..doing this under water. Don't try this at home :)")



nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.number_of_eyes)