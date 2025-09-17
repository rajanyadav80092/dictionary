num=int(input("enter a number:"))
i=2
while (i<num):
    if (num%i==0):
        print("not prime")
        break

    i+=1    
else:
    print("prime") 
print(i) 
print(num/i)