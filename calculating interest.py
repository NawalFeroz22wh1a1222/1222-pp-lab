p=int(input("principle amount:"))
r=float(input("rate of interest:"))
t=int(input("time period:"))
si=p*t*r
ci=p*pow((1+r/100),t)
print("the simple interest is:",si)
print("teh compund interest is:",ci)







