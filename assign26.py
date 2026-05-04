#python script to check given string has only alphabet
s=input("enter a string")
for ch in s:
    if ch>="a" and ch<="z" or ch>='A' and ch<="Z":
        pass
    else:
        print("string has some character other than a alphabet")
        break
else:
    print("string has only alphabet")