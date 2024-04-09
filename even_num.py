def find_even_nums(num):
 # Use a list comprehension to generate even numbers from 1 to num
 return [x for x in range(1, num + 1) if x % 2 == 0]

print(find_even_nums(8))
print(find_even_nums(4))
print(find_even_nums(2))