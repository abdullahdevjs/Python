def factorial():
    f=1
    print("enter the number")
    number=int(input())
    for i in range(1,number+1):
        f=f*i
        print(f)
factorial()