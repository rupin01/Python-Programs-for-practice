def square_digits(n):
  """
  Squares each digit of a number and returns the new number.

  Args:
      n: An integer.

  Returns:
      A new integer with each digit squared.
  """
  # Convert the number to a string
  str_n = str(n)

  # Square each digit and build the new number string
  new_str = ""
  for digit in str_n:
    new_str += str(int(digit) ** 2)

  # Convert the new string back to an integer
  return int(new_str)

# Examples
print(square_digits(9119))  # Output: 811181
print(square_digits(2483))  # Output: 416649
print(square_digits(3212))  # Output: 9414
