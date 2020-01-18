from  random import seed
from random import random
l = list()
W = int(input("Enter the width for bin =")) # width for bin
H = int(input("Enter the height for bin =")) # height for bin
w = int(input("Enter the width for iteam =")) # width for iteam
h = int(input("Enter the width for iteam =")) # width for iteam
if w!=0 | h!=0 | W!=0 | H!=0:
    A = W * H # area for bin
    print(A)
    a = w * h # area for iteam
    print(a)
    if a <= A:
        b = l.append(a) # iteam is placed into bin
        seed(b)
        print(random())


