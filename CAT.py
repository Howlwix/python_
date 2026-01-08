class Cat:
    def __init__(self, name = str, color = str, energy = int):
        self.energy = energy
        self.name = name
        self.color = color
    def meow(self):
        return "Meow"
    def eat(self):
        if self.energy < 100:
            self.energy += 100-self.energy
            return "Eat"
        else:
            return "Not Eat"
cat1 = Cat("red", "white",50)
cat2 = Cat("blue", "black",100)
cat3 = Cat("green", "white",40)
print(cat3.meow())
print(cat3.energy)