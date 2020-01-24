name = input("Enter any name =")

if name == "Max":
    print("Your Entered  name:" , name)
elif name == "Leo":
    print("Your Enterd name :" , name)
elif name == "King":
    print("Your entered name :", name)
elif name == "Roy":
    print("Your Entered name :", name)
else:
    print("Your Entered name is invalid")
# 2nd program
x = int(input("Enter any number"))
if x < 0:
    print("x is negitive")
else:
    print("x is positive")
    if x % 2 == 0:
        print("x is even")
    else:
        print("x is odd")

# Even number b /w serise
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count_even = 0
count_odd = 0
for x in numbers:
    if x % 2 == 0:
        count_even+=1
    else:
        count_odd+=1

print("The total even number :", count_even)
print("The total odd number :", count_odd)

# find a data type in list
datalist = [1452, 11.22 , 1+2j ,True , 'Qurat' , (0 ,-1) , [1 , 5], {"class":'V', "section":'A'}]
for item in datalist:
    print("Type of" , item , "is", type(item))
# print the number expect 3 and 6
for x in range(6):
    if (x == 3 or x==6):
        continue
    print(x,end=' ')
print("\n")
# print fabnoki serise
x,y = 0, 1
while y < 50:
    print(y)
    x,y = y, x+y

#fizzbuzz print
for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)






