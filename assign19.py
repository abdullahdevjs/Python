# sum of first n natural number
n =int(input("enter a number"))
s=0
for i in range(1, n+1):
    s=s+i
print("sum is",s)

#Q2 square of first n natural number
n=int(input("enter a  number"))
s=0
for i in range(1,n+1):
    s=s+i**2
print("sum of square",s)

#Q3 sum of first n cube 
n=int(input("enter a number"))
s=0
for i in range(1,n+1):
    s=s+i**3
print("sum of cube",s)

#Q4 sum of odd first n natural number
n=int(input("enter a number"))
s=0
for i in range(1,n+1):
    s=s+2*i-1
print("sum of ",s)