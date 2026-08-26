number=int(input("enter number"))
for i in range(2,number):
    if number%i==0:
        print("not prime")
        break
else:
    print("given number is prime number")

number1=int(input("enter first number"))
number2=int(input("enter first number"))
for i in range(number1+1,number2):
    for j in range(2,i):
        if i%j==0:
            
            break
    else:
        print("prime",i)