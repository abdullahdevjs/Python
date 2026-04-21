"""print all the character in a string and stop printing if 'r' appeared in a sequence
if all character succesfully printed then print a message all the characyer are proceed"""
n=input("enter a string")
for ch in n:
    if ch=='r':
        break
    print(ch)
else:
    print("all the character are proceed")