# program 6 - GRADES

p = float(input("enter percentage:"))

if p >= 65 and p <=100:print('Excellent') 
elif p < 65 and p >= 55: print('Good')
elif p < 55 and p >= 40:print('Fair')
elif p < 40:print('Failed')

else:
    print("Enter only Percentage Between 1 to 100")
