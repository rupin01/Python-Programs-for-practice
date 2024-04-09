#calculateLength() will count the digits present in a number    
def calculateLength(n):    
    length = 0;    
    while(n != 0):    
        length = length + 1;    
        n = n//10;    
    return length;    
     
#sumOfDigits() will calculates the sum of digits powered with their respective position    
def sumOfDigits(num):    
    rem = sum = 0;    
    len = calculateLength(num);    
        
    while(num > 0):    
        rem = num%10;    
        sum = sum + (rem**len);    
        num = num//10;    
        len = len - 1;    
    return sum;    
      
result = 0;    
     
#Displays all disarium numbers between 1 and 100    
print("Disarium numbers between 1 and 100 are");    
for i in range(1, 101):    
    result = sumOfDigits(i);    
        
    if(result == i):    
        print(i),    