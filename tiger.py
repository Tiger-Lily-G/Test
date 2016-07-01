

class Animal(object):

    name = None
    size = None

    def roar(self):
        return 'RAAAAWWWR'

    def speak(self):
        return self.name + 'yay!'

    def add_these(self, num1, num2):
        return num1 + num2


class SuperAnimal(Animal):

    def superpower(self):
        return 'BLAST'


def test_animal_roars():
    animal1 = Animal()
    animal1.name = 'bob'

    assert animal1.roar() == 'RAAAAAWWWR'
