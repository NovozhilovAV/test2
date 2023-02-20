# print("Hello VOLODYA!!")
# a = 4 # a = 4
# c = 5 + 3 # a = 4, c = 8
# a = a + c # a = 12, c = 8
# c = a - 2  # a = 12, c = 10

# print(a)
# print(c)

#
class Child:  # МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ
    def callMama(self):
        print("MaMa!!")


class Cat:  # объявление класса
    def __init__(self, name, weight, color):  # указание на объект, возраст можно не писать
        self.name = name
        self.weight = weight  # поле
        self.__age = 0
        self.color = color

    def voice(self):  # метод класса
        print("meow!")

    # def get_age(self):  #
    #     return self.__age
    #
    # def set_age(self, newAge):
    #     self.__age = newAge

    # @property
    # def age(self):
    #     return self.__age
    #
    # @age.setter
    # def age(self, newAge):
    #     self.__age = newAge


a = Cat("Barsik", 3, "red")  # вызвали кота

print(a.color)
a.voice()


# print(a.get_age())
#
# a.set_age(5)
# print(a.get_age())

# print(a.age)
# a.age = 6
#
# print(a.age)

# q.voice()


class Kitten(Cat, Child):    # вызвали котенка
    def voice(self):
        print("Meee!")


q = Kitten("murzik", 1, "black")

q.callMama()
