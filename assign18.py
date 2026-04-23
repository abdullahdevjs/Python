n = int(input("Enter count: "))

num = 2
count = 0

while count < n:
    flag = 0
    for i in range(2, num):
        if num % i == 0:
            flag = 1
            break

    if flag == 0:
        print(num, end=" ")
        count += 1

    num += 1