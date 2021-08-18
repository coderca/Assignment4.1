#class variables
#instance varibales


class person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        person.number_of_people = person.number_of_people + 1

p = person("tim")
print(p.name)
p1 = person("sam")
p2 = person('tom')
print(p1.name)
print(p2.name)
print('\n')

# self points to instacne of the class
#cls points to the class name
#alternative constructor


class person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        person.number_of_people = person.number_of_people + 1

    def add(self):
        print("add method")

    @classmethod
    def get_num_of_ppl(self):
        return self.number_of_people

p_1 = person('tim')
p_2 = person('tom')
print(person.get_num_of_ppl())
#static method we dont use self and cls

class person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        person.number_of_people = person.number_of_people + 1

    def add(self):
        print("add method")

    @classmethod
    def get_num_of_ppl(cls):
        return cls.number_of_people


# staticmethod
class math:

    def add(self, x):
        return x + 1

    @staticmethod
    def add_5(x):
        return x + 5

    @staticmethod
    def add_10(y):
        return y + 10


class math:
    pi = 3.14

    # normalmethod
    def add(self, x):
        return x + 1

    @classmethod
    #classmethod
    def add_5(cls):
        return cls.pi

    @staticmethod
    #staticmethod
    def add_20(y):
        return y + 20

#memory mgmt
x = 10
print(id(x))
print(hex(id(x)))
string = 'hello'
print(id(string))
print(hex(id(string)))
y = x
print(id(y))
#10  ,x and y too the same mem location

import sys
print(sys.getsizeof(x))
print(sys.getsizeof(y))
print(sys.getsizeof(string))

#python as oevrheads - reference to the obj type of obj

str = ''
print(sys.getsizeof(str))


str1 = 'a'
print(sys.getsizeof(str1))

list = []
print(sys.getsizeof(list))

list1= [1] #returns 8 bytes it has the poiter or reference to the elemets tp the list
print(sys.getsizeof(list1))

list1= [1,2]
print(sys.getsizeof(list1))

x =10
print(id(x))
x = 11
print(id(x))
#the methods are variables created on stack mem
#the  objs and ninstacne variables are created on heap
#a new stack frame is created on invocation of a function