number = int(input("Enter number: "))

s = 0
original = number

while number > 0:
    digit = number % 10
    s = s + digit ** 3
    number = number // 10

if s == original:
    print("Given number is Armstrong")