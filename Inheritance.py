# Function Overriding
# Python doesn't support method overloading

from math import pi

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        pass

    def whichShape(self):
        print(self.name)

class Square(Shape):
    def __init__(self, name, length):
        # Calling constructor of Base Class
        # Shape.__init__(self,name)
        super().__init__(name)
        self.side_length = length

    def area(self):
        print(self.side_length**2)

    def fact(self):
        print("Square has each angle equalt to 90 degrees")

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.circle_radius = radius

    def area(self):
        print(pi * (self.circle_radius**2))

sq = Square("Square", 4)
cr = Circle("Circle", 5)
sq.area()
cr.area()
sq.fact()
cr.fact()
sq.whichShape()
cr.whichShape()



# Multiple inheritance

class xyz:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def test(self):
        print("This is a test meth from xyz")


class xyz1:
    def __init__(self,p,q,r):
        self.p=p
        self.q=q
        self.r=r

    def test1(self):
        print("This is a test1 meth from xyz1")


class child(xyz1,xyz):  # by default child class will show varibles from 1st class only
    def __init__(self,*args,**kwargs):
        xyz.__init__(self,*args)
        xyz1.__init__(self,**kwargs)


n = child(1,2,3,p=4,q=5,r=6)
print(n.a)
print(n.b)
print(n.c)
print(n.p)
print(n.q)
print(n.r)


# Public, private, protected variables
class test:
    def __init__(self,a,b,c):
        self._a=a     # _a is protected variable and can be accessed within class and sub class
        self.__b=b    # __b is private variable
        self.c=c      # c is public variable

class test1(test):
    pass

v=test1(100, 200, 300)
print(v._a)
# print(v._test1__b)   # private variables can not be used in sub class
print(v._test__b)      # but can be used like this
print(v.c)

v._a = 1000
v.__b = 2000           
v.c = 3000
print(v._a)
print(v.c)
print(v._test__b)
v._test__b = 2000      # private variables can be modified like this
print(v._test__b)


