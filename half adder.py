def half_adder(c,d):
    s=c^d
    c=c&d
    return(s,c)
a = int(input())
b = int(input())
print(half_adder(a,b))