# loops and list

c=[1,2,3,4,7]
fruits=['apple','bannaa','orange','grapes']
e=[1,'er',2,'rtefg',12,'seafsedgasfged']

for number in c:
    print("this is %d count" %number)
for fruit in fruits:
    print("a fruit of type %s" %fruit)
for i in e:
    print("I got %r" %i)

elements=[]
for i in range(0,6):
    a=input("enter %d element" %(i+1))
    elements.append(a)
for i in elements:
    print(elements)

