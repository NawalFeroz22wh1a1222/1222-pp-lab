alpha="abcdefghijklmnopqrstuvwxyz"
s=input("enter input:")
a=s.islower()
b=s.isupper()
c=s.isdigit()
for i in s:
    if a:
        print("lower case")
    elif b:
        print("upper case")
    else:
        if c:
            print("digit")
        else:
            print("special character")
