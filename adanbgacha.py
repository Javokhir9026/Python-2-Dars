import os
os.system("cls")

a = int(input("A: "))
b = int(input("B: "))

while(a <= b):
    if(a % 11 == 0 and a % 3 == 0 and a % 9 == 0):
        print(a, end=" ")
    a+=1