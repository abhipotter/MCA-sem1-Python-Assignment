class Animal:
    def eat(self):
        print('Eating')

class Dog(Animal):
    def bark(self):
        print('Barking')

class Cat(Animal):
    def meow(self):
        print('Meowing')

d = Dog()
c = Cat()
d.eat()
d.bark()
c.eat()
c.meow()
