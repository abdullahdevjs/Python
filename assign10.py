# program to check given character is vowel or not by match case

x = input("enter a character: ").lower()

match x:
    case x if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        print("vowel")
    case _:
        print("consonant")