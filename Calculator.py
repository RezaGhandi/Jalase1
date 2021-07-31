import math

op=input("Enter math operations:")

if op == 'sin' or op == 'cos' or op == 'sqrt' or op == 'tan':
    a=float(input("Enter Number:"))

else:
    a=float(input("Enter first number:"))
    b=float(input("Enter second number:"))

if op == "+":
    result=(a+b)
elif op == "-":
    result=(a-b)
elif op == "*":
    result=(a*b)
elif op == "/":
    if b == 0:
        result="you can not divide by zero"
    else:
        result=(a/b)
elif op == "sin":
    x=(a/180)*3.141592653589793
    result=math.sin(x)
elif op == "cos":
    result=math.cos(a)
elif op == "sqrt":
    result=math.sqrt(a)
elif op == "tan":
    x=(a/180)*3.141592653589793
    result=math.tan(x)

print(result)
