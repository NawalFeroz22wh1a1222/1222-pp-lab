import re
a = input("enter a phone no: ")
if len(a) == 13 or len(a) == 12:
    x=re.findall("^040|91",a)
    if x == ['040']:
        print("starts with 040")
        b=re.split("0",a,2)
        if len (b[2]) == 10:
            o = b[2]
            n=re.findall("\d",o)
            if len(n) == 10:
                print("a valid phone no")
            else:
                print("not a alid phone no")
        else:
            print("not valid")
    elif x == ['91']:
        print("starts wiht 91")
        u=re.split('1',a,1)
        if len(u[1]) == 10:
            k=u[1]
            m=re.findall("\d",k)
            if len(m) == 10:
                print("valid phone no")
            else:
                print("not valid phone no")
        else:
            print("not valid")
    elif x == []:
        print("enter valid starting code")
else:
    print("not valid")        


                    

