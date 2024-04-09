def is_symmetrical(num):
 # Convert the number to a string
 num_str = str(num)

 # Check if the string is equal to its reverse
 return num_str == num_str[::-1]

print(is_symmetrical(12567))
print(is_symmetrical(7227))
print(is_symmetrical(444444444444444))
print(is_symmetrical(4444444444))
print(is_symmetrical(111121111))