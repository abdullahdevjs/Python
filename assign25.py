#python script to print first n even number in a lis
l1=[2*x for x in range(1,int(input("enter the number"))+1)]
print(l1)

#Q2 fabinocii series in a list
n=int(input("enter a number"))
fib=[]
a=-1
b=1
while n:
    c=a+b
    fib.append(c)
    a=b
    b=c
    n-=1
print(fib)