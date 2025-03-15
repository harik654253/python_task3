# program 9 - library

d = int(input("enter the number of days :"))

if d <= 5 :
    c= d * 2
    print('Rent Amount is :', c)
elif d >= 6 and d <= 10:
    c= d * 3
    print('Rent Amount is :', c)
elif d >= 11 and d <= 15:
    c= d * 4
    print('Rent Amount is :', c)    
else:
    c= d * 5
    print('Rent Amount is :', c)
