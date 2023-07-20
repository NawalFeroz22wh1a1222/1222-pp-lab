import re
a =  input("enter a phone no")
if len(a) == 10:
    x = re.findall("\d",a)
    if len(x) == 10:
        print("valid phone no")
    else:
        print("invalid phone no")
else:
    print("not valid")
