a=int(input("enter first number:"))
operator=input("enter the operator;+,-,*,/,%")
b=int(input("enter second number:"))
def sum(a,b):
    if (operator=="+"):
        return a+b
def sub(a,b):
    if (operator=="-"):
        return a-b
def mul(a,b):
    if (operator=="*"):
        return a*b
def div(a,b):
    if (operator=="/"):
        return a/b
def mod(a,b):
    if (operator=="%"):
        return a%b
print("the result is:",sum(a,b)or sub(a,b) or mul(a,b) or div(a,b) or mod(a,b))

