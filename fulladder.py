def half_adder(a,b):
    s=a^b
    d=a&b
    return (s,d)
a=int(input())
b=int(input())
c=int(input())
def full_adder(x,y,z):
    s1,c1=half_adder(x,y)
    s2,c2=half_adder(s1,z)
    return(s1,c1|c2)
print(full_adder(a,b,c))