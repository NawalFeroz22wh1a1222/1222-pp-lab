n=int(input("enter a no."))
a=0
b=1
c=0
count=1
while(count<=n):
    print(c,end=" ")
    count+=1
    a=b
    b=c
    c=a+b

