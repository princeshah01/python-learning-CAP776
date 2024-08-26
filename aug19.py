# arthmetic calculator

a = int(input("enter a number"))
b = input("enter a operator")
c = int(input("enter a 2nd number")) 

if (b=="*"):
    print(a*c)
elif(b=="+"):
    print(a+c)
elif(b=="-"):
    print(a-c)
elif(b=="/"):
    print(a/c)        
else:
    print("invalid oprator")
