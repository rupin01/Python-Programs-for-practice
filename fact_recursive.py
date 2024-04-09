def factorial(n):
  """
  Calculates the factorial of a number recursively.

  Args:
      n: The non-negative integer for which to calculate the factorial.

  Returns:
      The factorial of n.
  """

  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

# Examples
print(factorial(5))  # Output: 120
print(factorial(3))  # Output: 6
print(factorial(1))  # Output: 1
print(factorial(0))  # Output: 1
