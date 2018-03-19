#prime
print(" enter the number \n")
num=int(input())
if  num > 1:
    for i in range(2,num):
        if(num%i==0):
            print("not prime \n")
            break
    else:
        print("prime \n")
else:
    print("invalid input")
