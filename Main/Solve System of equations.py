eq1 = eval(input("Enter the co-efficients of first equation"))
eq2 = eval(input("Enter the co-efficients of second equation"))

a1,b1,c1 = eq1
a2,b2,c2 = eq2
try:
    x = ((b2*c1) - (b1*c2))/((a1*b2) - (a2*b1))
    y = ((a1*c2) - (a2*c1))/((a1*b2) - (a2*b1))

    print("x:",x)
    print("y:",y)
except:
    print("No solution")