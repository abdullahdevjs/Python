#write a python script to display all prime numbers within a range. 
#range start=15 end=45
print("enter two numbers")
beg=int(input())
end=int(input())
for num in range(beg,end):
    for i in range(2, num):
        if num%i==0:
            break
    else:
        print(num)