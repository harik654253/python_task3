# program 8 - numbers and operators

a = int(input("enter first number : "))
b = int(input("enter second number : "))
c = input("operator : ")

if c == '+' :
    d = a + b
    print('Addition of numbers is :', d)
elif c == '-' :
    d = a - b
    print('Subtraction of numbers is :', d)
elif c == '*' :
    d = a * b
    print('Multiplication of numbers is :', d)
elif c == '/' :
    d = a / b
    print('Division of numbers is :', d)
elif c == '//' :
    d = a // b
    print('Floor Division of numbers is :', d)
elif c == '%' :
    d = a % b
    print('Modulo of numbers is :', d)
elif c == '**' :
    d = a ** b
    print('power of numbers is :', d)
      
else:
    print('Invalid operator')
