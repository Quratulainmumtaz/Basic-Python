def sum(arg1, arg2):
    if type(arg1)!= type(arg2):
        print("Please give the same data value")
        return
    return(arg1 + arg2)

a = sum(15 , 30)
print(a)
b = sum("Hellow" , "World")
print(b)
c = sum(17.4, 30.6)
print(c)
d = sum("hellow", 15)
print(d)
#simple print name and age of person in function
def student(name, age, **marks):
    print("Name", name)
    print("age", age)
    print('marks',marks)
    for key, value in marks.items():
        print(key, '' , value)
student('Qurat', 24 , English=92, Math=30 , Physic=30, Computer=100)
#write a program print max number in the function
def max(x, y , z):
    if x > y and x > z:
        return x
    if y > z and y > z:
        return y
    if z > x and z > x:
        return z
print(max(2, 15 , 30))
#print the sum all in list
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))
#print all the multipal of numbers
def multipal(numbers):
    total = 1
    for x in numbers:
        total *= x
    return  total
print(multipal((2,4,5,67)))
#print number in range or not
def num_range(n):
    if n in range(3 , 9):
        print("The number in range of 3 and 9", n)
    else:
        print("The number is not in Range")
num_range(5)

#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def string_check(s):
    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"] += 1
        elif c.islower():
            d["LOWER_CASE"] += 1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["UPPER_CASE"])
    print("No. of Lower case Characters : ", d["LOWER_CASE"])
string_check("Qurat Ul Ain Mumtaz")
#Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x

print(unique_list([1,2,3,4,4,4,5,6,6,7,8,9,9,10]))
#Write a Python program to print the even numbers from a given list.
def enum(l):
    Evennum = []
    for n in l:
        if n % 2 == 0:
            Evennum.append(n)
    return Evennum
print(enum([2, 3, 4, 5, 6 ,7,8]))


