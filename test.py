print("This is a calculator program ")
a=int(input("Enter your first number : "))
b=int(input("Enter your second number:"))

def add(a,b):
    print(a+b)

def mul(a,b):
    print(a*b)

inp=input("Which opertaion you want to perform : ")

if inp=="add":
    add(a,b)
else:
    mul(a,b)