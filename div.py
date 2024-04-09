#division

num3=float(input("Enter the dividend: "))
num4=float(input("Enter the divisor: "))
if num4==0:
    print("Error:Division by zero is not allowed.")
else:
    div_result=num3/num4
    print(f"Division:{num3}/{num4}={div_result}");
