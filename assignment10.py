#question1
class Animal():
    def animal_attribute(self):
        print("save tiger")
class Tiger(Animal):
    print("Tiger is national animal of India ")
tig=Tiger()
tig.animal_attribute()

#question2
#output is given as following:
#print a.f() :  A
#print  b.f() : B

#question3

class Cop():
    def __init__(self,name,age,work,experience,designation):
        self.n=name
        self.a=age
        self.w=work
        self.e=experience
        self.d=designation
    def display(self):
        print(self.n)
        print(self.a)
        print(self.w)
        print(self.e)
        print(self.d)
    def update(self,name,age,work,experience,designation):
        self.na = name
        self.ag = age
        self.wo = work
        self.ex = experience
        self.de = designation
        print(self.na)
        print(self.ag)
        print(self.wo)
        print(self.ex)
        print(self.de)

class Mission(Cop):
    def add__mission__details(self):
        print("mission impossible")
c=Cop("mohit",21,"hardwork",22,"DC")
m=Mission("mohit",21,"hardwork",22,"DC")
m.display()
m.update("sharma",21,"busy",22,"IG")

#question4

class Shape():
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
class Rectangle(Shape):
    def Area(self):
        area=(self.l)*(self.b)
        print(area)
class Square(Shape):
    def Area(self):
        AREA=(self.l)*(self.l)
        print(AREA)
s=Shape(12,8)
r=Rectangle(12,8)
r.Area()
sq=Square(12,12)
sq.Area()




