# student grade mgmt system
class Stu:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Cor:
    def __init__(self, name, max_stu):
        self.name = name
        self.max_stu = max_stu
        self.students = []

    def add_stu(self, student):
        if (len(self.students) < self.max_stu):
            self.students.append(student)
            return True
        return False

    def avg_grade(self):
        value = 0
        for s in self.students:
            value = value + s.get_grade()

            return value / len(self.students)

    def add_num(self, x):
        print(x + 1)


s1 = Stu("ti",20,80)
s2 = Stu("j",34,60)
print(s1.name)
print(s2.name)
print(s1.get_grade())
print(s2.get_grade())
print(s1.__dict__)
print(s2.__dict__)
c1 = Cor('CSE',2)
print(c1.__dict__)
c1.add_stu(s1)
c1.add_stu(s2)
print(c1.__dict__)
print(c1.avg_grade())

print('\n')
class pet:

    def __init__(self, age, name):
        self.age = age
        self.name = name


    def show(self):
        print(f'{self.name} {self.age}')


# inhertitance
class D(pet):

    def speak(self):
        print("bark")


class C(pet):

    def __init__(self, age, name, color):
        super().__init__(age, name)
        self.color = color

    def show(self):
        print(f'{self.name} {self.age} {self.color}')

    def speak(self):
        print("meow")


d1 = D(20,"bil")
d1.speak()
d1.show()
c1 = C(20,"tom",'black')
c1.speak()
c1.show()
p1 = pet("tom",10)
p1.show()
d1.show()
c1.show()
c3 = C(90,"forno","white")
c3.__dict__
c3.show()


class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)

t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()