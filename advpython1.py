help(str)


class Dog:
    pass


class Dog:
    def speak(self):
        print('bark')

    def walk(self):
        print('walk')


d = Dog()
print(d.speak())
print(d.walk())

d1 = Dog()
print(d1.speak())
print(d1.walk())

print(type(d))
help(d)
help(d1)
d.name = 'billy'
d1.name = 'tom'

print(d1.name)


class pet:

    def speak(self):
        print('meow')


p = pet()
print(type(p.speak()))


class Dog1:
    def bark(self):
        print('bark')

    def set_breed(self, breed):
        self.breed = breed

    def get_breed(self):
        return self.breed


print(Dog1.__doc__)
d2 = Dog1()
d3 = Dog1()
d2.set_breed("Dalmation")
print(d2.get_breed())
d3.set_breed('husky')
print(d3.get_breed())


# init method

class Dog2:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def bark(self):
        print('bark')


d5 = Dog2('timmy', 20, 'black')
print(d5.name)
print(d5.age)
print(d5.color)
d5.bark()


class Vehicle:
    # Class attribute
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


School_bus = Bus("School Volvo", 200, 19)
print(School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

car = Car("Audi Q7", 280, 20)
print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)
