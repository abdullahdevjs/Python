#digit count
n=int(input("enter a number"))
count=0
while n:
    n=n//10
    count=count+1
print(count)

#Q sum of digit
n=int(input("enter a number"))
s=0
while n:
    r=n%10
    s=s+r
    n=n//10
print("sum of digit",s)