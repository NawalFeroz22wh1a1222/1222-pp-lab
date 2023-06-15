def binaryNum(n,s,ones,zeros):
    if(len(s)==n):
        print(s)
        return
    if(ones<n/2):
        binaryNum(n,s+"1",ones+1,zeros)
    if(zeros<n/2):
        binaryNum(n,s+"0",ones,zeros+1)
s=""
binaryNum(3,s,0,0)