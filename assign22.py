#print only vowels in a string
s=input("enter a string")
for ch in s:
    if ch in "aeiouAEIOU":
        print(ch)


#Q count spaces in a string
s=input("enter a string")
count=0
for ch in s:
    if ch==' ':
        count+=1
print("count=",count)