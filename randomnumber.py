import random

comp=random.randint(1,10)
print("guess the value 1 to 10")

while True:
    user=int(input("enter a number:"))
    if user == comp :
        print("congratulation you are genius")
        break
    elif (user<comp):
        print("low to reach the main target")
    else:
        print("try again")