# lcm of a number
number1=int(input("enter first number")) #taking input from user
number2=int(input("enter second number")) #taking input from user
greater=max(number1,number2)
while True:
    if greater%number1==0 and greater%number2==0:
        break
    greater+=1
print("the lcm of a given number=",greater)
    