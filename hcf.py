# lcm of a number
number1=int(input("enter first number")) #taking input from user
number2=int(input("enter second number")) #taking input from user
smaller=min(number1,number2)
while True:
    if number1%smaller==0 and number2%smaller==0:
        break
    smaller-=1
print("the hcf of a given number=",smaller)
    