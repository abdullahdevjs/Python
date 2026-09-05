n=int(input("enter number"))
lst=[]
for i in range(n):
    lst.append(int(input("enter score")))

lst.sort()
print(lst[1])
    