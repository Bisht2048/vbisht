from tkinter import *

while True:
    a=int(input("Enter a Number here: "))
    e = input("+,-,x,/ : ")
    b=int(input("Enter a number here: "))

    if e=="+":
        print(a,e,b,"=",a+b)
    elif e=="-":
        print(a,e,b,"=",a-b)
    elif e=="x" or e=="X":
        print(a,e,b,"=",a*b)
    elif e=="/":
        print(a,e,b,"=",a/b)
    else:
        print("Error")


# a=input("Enter here: ")
# a=int(a)
# print(a)

