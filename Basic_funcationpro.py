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
