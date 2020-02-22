class car:
    pass
ford = car()
Honda = car()
audi = car()

ford.speed = 300
Honda.speed = 400
audi.speed = 350

ford.color = 'red'
Honda.color = 'yellow'
audi.color = 'black'

print(ford.speed)
print(ford.color)
print(Honda.speed)
print(Honda.color)


#print the rectangle high and width
class rectangle:
    pass
rect1 = rectangle()
rect2 = rectangle()

rect1.highet = 20
rect1.width = 30

rect2.highet = 30
rect2.width = 40
print(rect1.highet * rect1.width)
print(rect2.highet * rect2.width)
#Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.
class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * 3.14

    def perimeter(self):
        return 2 * self.radius * 3.14


NewCircle = Circle(8)
print(NewCircle.area())
print(NewCircle.perimeter())
#area of rectangulr
class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

newRectangle = Rectangle(12, 10)
print(newRectangle.rectangle_area())
#Write a Python class which has two methods get_String and print_String. get_String accept a string
# from the user and print_String print the string in upper case.
class IOString():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input("Enter any string in lowercase")

    def print_String(self):
        print(self.str1.upper())

str1 = IOString()
str1.get_String()
str1.print_String()
#Write a Python program to reverse a string word by word.
class py_solution:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))


print(py_solution().reverse_words('hello .py'))












