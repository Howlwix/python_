class Cat:
    def __init__(self, name = str, color = str, energy = int):
        self.energy = energy
        self.__name = name
        self.color = color
    def meow(self):
        return "Meow"
    def eat(self):
        if self.energy < 100:
            self.energy += 100-self.energy
            return "Eat"
        else:
            return "Not Eat"
    def get_name(self):
        return self.__name
cat1 = Cat("red", "white",50)
cat2 = Cat("blue", "black",100)
cat3 = Cat("green", "white",40)
print(cat1.get_name())
class ShortHairCat(Cat):
    def __init__(self, name=str, color=str, energy=int):
        super().__init__(name, color, energy)
print(cat2.get_name())
class LongHairCat(Cat):
    def __init__(self, name=str, color=str, energy=int):
        super().__init__(name,color,energy)
print(cat3.get_name())
print(cat3.energy)