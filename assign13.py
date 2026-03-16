#write a program if user enter a even number he won the game and if user enter a odd no give him three chance at most after he lost
i=1
while i<=3:
    a=int(input("enter a number"))
    if a%2==0:
        print("won")
        break
    i=i+1
if i==4:
    print("lost")