# Задача "Съедобное, несъедобное"

class Animal:
    def __init__(self, name, alive=True, fed=False):
        self.name = name
        self.alive = alive # alive=True - живой
        self.fed = fed # fed=False - накормленный

    def eat(self, food):
        food = Plant(self.name)
        edible = Plant(edible=False)
            if edible is True:
                print()

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Plant:
    def __init__(self, name, edible=False):
        self.name = name
        self.edible = edible # съедобность



class Flower(Plant):
    pass

class Fruit(Plant):
    pass

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
