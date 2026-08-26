number=int(input("enter number"))
for i in range(2,number):
    if number%i==0:
        print("not prime")
        break
else:
    print("given number is prime number")