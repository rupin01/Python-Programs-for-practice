def list_operation(x, y, n):
 # Use list comprehension to generate the list of numbers divisible by n
 return [num for num in range(x, y + 1) if num % n == 0]

print(list_operation(1, 10, 3))
print(list_operation(7, 9, 2))
print(list_operation(15,20,7))