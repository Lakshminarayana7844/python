g=input("enter the grade=")
s=int(input("enter the salary="))
if s<=0:
    
    print("enter the salary=")
elif g=="B":
    
    print("salary=",s)
    
    print("bonus=",(10/100)*s)
    
    print("toatl to be paid=",((10/100)*s)+s)
    
elif g=="A":

    print("salary=",s)
    
    print("bonus=",(5/100)*s)
    
    print("toatl to be paid=",((5/100)*s)+s)
    
elif s<=10000:
    
    print("salary=",s)
    
    print("bonus=",(2/100)*s)
    
    print("toatl to be paid=",((2/100)*s)+s)
    
else:
    print("invalid input")
