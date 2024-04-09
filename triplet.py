def is_triplet(a, b, c):
  """
  Checks if three numbers form a Pythagorean triplet.

  Args:
      a: The first integer.
      b: The second integer.
      c: The third integer.

  Returns:
      True if the numbers form a Pythagorean triplet, False otherwise.
  """
  # Sort the numbers in ascending order
  numbers = sorted([a, b, c])

  # Check if the equation a^2 + b^2 = c^2 holds
  return numbers[0]**2 + numbers[1]**2 == numbers[2]**2

# Examples
print(is_triplet(3, 4, 5))  # Output: True
print(is_triplet(13, 5, 12))  # Output: True
print(is_triplet(1, 2, 3))  # Output: False
