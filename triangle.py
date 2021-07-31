a=int(input("Enter the size of the first side:"))
b=int(input("Enter the size of the second side:"))
c=int(input("Enter the size of the third side:"))

if a+b>c and a+c>b and c+b>a:
    result=("The triangle can be drawn")

else:
        result=("The triangle cannot be drawn")

print(result)
