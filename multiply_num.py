def multiply_nums(nums):
  """
  Multiplies numbers in a comma-separated string and returns the product.

  Args:
      nums: A string containing comma-separated numbers.

  Returns:
      The product of the numbers in the string.
  """
  # Split the string into a list of numbers
  numbers = [float(num) for num in nums.split(", ")]

  # Multiply all the numbers in the list
  product = 1
  for num in numbers:
    product *= num

  return product

# Examples
print(multiply_nums("2, 3"))  # Output: 6
print(multiply_nums("1, 2, 3, 4"))  # Output: 24
print(multiply_nums("54, 75, 453, 0"))  # Output: 0
print(multiply_nums("10, -2"))  # Output: -20
