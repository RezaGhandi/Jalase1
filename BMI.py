import math
h=float(input("type ypur height(cm)"))
w=float(input("type your weight(kg)"))

h=h/100

bmi=w/(math.pow(h, 2))

if bmi<18.5:
    print("your BMI is", bmi ,"and you are underweight!")

elif bmi>=18.5 and bmi<=24.99:
    print("your BMI is", bmi ,"and you are normal")

elif bmi>=25 and bmi<=29.99:
    print("your BMI is", bmi ,"and you are overweight!")

elif bmi>=30 and bmi<=34.99:
    print("your BMI is", bmi ,"and you are obese!")

elif bmi>=35:
    print("your BMI is", bmi,"and you are extremely obese!!")