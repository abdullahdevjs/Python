#print only vowels in a string
s=input("enter a string")
for ch in s:
    if ch in "aeiouAEIOU":
        print(ch)