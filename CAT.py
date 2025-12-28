class Cat:
    def __init__(self, name = str, color = str, meow = str, eat = str):
        self.name = name
        self.color = color
        self.meow = meow
        self.eat = eat
    def is_meow(self):
        return self.meow
    def is_eat(self):
        return self.eat
cat1 = Cat("red", "white", "meow", "not eat")
cat2 = Cat("blue", "black", "not meow", "eat")
cat3 = Cat("green", "white", "not meow", " not eat")
print(cat3.is_meow())
print(cat2.is_eat())