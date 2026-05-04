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

# python script to check given chracter is present in astring or not
s=input("enter a sring")
ch=input("enter a charcter")
if ch in s:
    print("ch is present in s",ch)
else:
    print("ch is not present in s",ch)