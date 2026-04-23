# check whether the given number is prime or not
n=int(input("enter an number"))
for i in range(2,n):
    if n%i==0:
        print("given number is not a prime number")
        break
else:
    print("given number is a prime number")