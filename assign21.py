#digit count
n=int(input("enter a number"))
count=0
while n:
    n=n//10
    count=count+1
print(count)