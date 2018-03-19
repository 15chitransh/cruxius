#print series 2,5,11,23....
num=2
print("enter the number of terms in series")
n=int(input())
for i in range(0,n):
    print(num)
    num=num*2 +1
