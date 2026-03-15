#write a program to check the given quadratic equation have real rool or distinct root
print("enter the value of a, b, c")
a=int(input())
b=int(input())
c=int(input())
d=b**2-4*a*c
if d>0:
    print("two real and distinct root")
elif d==0:
    print(" two real and equal root")
else:
    print("roots are imaginary")