class Animal:  # объявление класса
    def __init__(self, age, color):  # указание на объект
        self._age = 0
        self._color = color

    def voice(self):  # метод класса
        print("Animal!")


    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, newAge):
        self._age = newAge

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, newColor):
        self._color = newColor


class Cat(Animal):
    def purring(self):
        print("Mrrrr!")   # добавили метод мурчания


class Tiger(Cat, Animal):
    def voice(self):   # переопределили метод
        print("RRRrrrrr!")


class Lion(Cat, Animal):
    def voice(self):  # переопределили метод
        print("LION GAWWWWW")
        # переопределить метод звука


class Ocelot(Cat, Animal):
    pass    # метод мурчания и звука не делают ничего


class DomCat(Cat, Animal):    # добавили метод прошения корма
    def meat(self):
        print("I'm hungry! Give me meat!!!")


class Dog(Animal):     # добавили метод прогулки
    def street(self):
        print("I walk")


class Child:
    def helpMama(self):
        print("Mama HELP ME!!")


class LionKitten(Lion, Cat, Animal, Child):
    pass


class Kitten(DomCat, Cat, Animal, Child):
    pass


class Puppy(Dog, Animal, Child):
    pass











