#Input two variables
a=input("Enter the value of first variable(a): ")
b=input("Enter the valu of the second variable(b):" )
#Display the original values
print(f"Original Values: a={a}, b={b}")
#Swap the values by using temporary variable
temp=a
a=b
b=temp
#display the swapped values
print(f"Swapped Values: a={a},b={b}")