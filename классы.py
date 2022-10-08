from itertools import product
from pprint import pprint
#Описать классом ваши личные данные:

class Person:
    def __init__(self, name, age, address, gender, weight, height):
        self.name, self.age, self.address, self.gender, self.height, self.weight = name, age, address, gender,  weight, height
        self.key = (name, address, gender)

    def __repr__(self):
        return "Person('%s', %s, '%s', '%s', %s, %s)" % (self.name, self.age, self.address, self.gender, self.weight, self.height)

egor = Person("Егор", 20, "Плеханова, 20, 50", 'Mужской', 86, 177)

people = {
    egor.key: egor,
}
pprint(people[egor.key])
pprint(people)
