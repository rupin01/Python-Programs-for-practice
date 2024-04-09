def bodmassindex(height, weight):
    return round((weight/height**2),2)

h=float(input("Enter the height in meters: "))
w=float(input("Enter the weight in kgs:"))

print("WElcome to BMI Calculator..")

bmi=bodmassindex(h,w)
print("Your BMI is: ",bmi)

if bmi<=18.5:
    print("You are underweight.")
elif 18.5 <bmi<=24.9:
    print("Your weight is normal.")
elif 25<bmi<=29.9:
    print("You are overweight.")
else:
    print("You are obese..")