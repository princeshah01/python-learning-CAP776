p = int(input("enter principle amount: "))
r = int(input("enter rate of interest: "))
t = int(input("enter time in year:  "))

si = (p*t*r)/100 
print(f"the simple interest for principle {p}  and rate {r} % in {t} years is : - {si} ")