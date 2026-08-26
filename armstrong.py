number = int(input("Enter number: "))

s = 0
original = number

while number > 0:
    digit = number % 10
    s = s + digit ** 3
    number = number // 10

if s == original:
    print("Given number is Armstrong")

number1 = int(input("enter number"))
number2 = int(input("enter 2nd number"))

for i in range(number1 + 1, number2):

    s = 0
    sum = i
    temp = i

    while temp > 0:
        digit = temp % 10
        s = s + digit ** 3
        temp = temp // 10

    if s == sum:
        print("the given number is armstrong", s)