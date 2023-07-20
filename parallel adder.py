def halfadder(c,d):
    s=c^d
    c=c&d
    return(s,c)
def fulladder(a,b,c):
    s1,c1=halfadder(a,b)
    s2,c2=halfadder(s1,c)
    return(s2,c1 or c2)
def paralleladder(c1):
    l=[[1,0],[1,0]]
    for i in range(0,len(l)):
        sum,c1 = fulladder(l[i][0],l[i][1],c1)
    return(sum,c1)
c1=int(input())
print(paralleladder(c1))    