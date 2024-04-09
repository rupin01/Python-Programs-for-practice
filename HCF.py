#Python program to find HCF of two numbers

def compute_hcf(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if((x%i==0) and (y%i==0)):
            hcf=i
        return hcf
num1=int(input("Enter the number: "))
num2=int(input("Enter the number: "))

print("The HCF is",compute_hcf(num1,num2))