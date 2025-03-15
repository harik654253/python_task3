# program 4 - GRADES

p2 = float(input("enter percentage:"))

if p2 > 80:print('GRADE A+') 
elif p2 <=80 and p2 > 60: print('GRADE A')
elif p2 > 50 and p2 <= 60:print('GRADE B+')
elif p2 > 45 and p2 <= 50:print('GRADE B')
elif p2 > 25 and p2 <= 45:print('GRADE C')
else:
    print("GRADE D")
