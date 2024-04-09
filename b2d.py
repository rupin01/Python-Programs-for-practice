def binary(decimal):
 binary_str = ""
 while decimal > 0:
   remainder = decimal % 2
 binary_str = str(remainder) + binary_str
 decimal = decimal // 2
 return binary_str if binary_str else "0"
print(binary(1))
print(binary(5)) 
print(binary(10)) 