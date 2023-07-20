import re
def validate_aadhar(a):
    if len(a) == 12:
        x=re.findall("\d",a)
        if len(x) == 12:
            return True
        else:
            return False
    else:
        print("wrong input")
        
a=input("enter aadhar number")
if validate_aadhar(a):
    print("valid")
else:
    print("not valid")        