#program to check given year is leap year or not
year=int(input("enter year number"))
if year%100==0:
    if year%400==0:
        print("leap year")
    else:
        print("non leap year")
else:
    if year%4==0:
        print("leap year")
    else:
        print("non leap year")