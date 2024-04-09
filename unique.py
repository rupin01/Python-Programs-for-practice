def unique(numbers):
  """
  Finds the unique number in a list where all others are the same.

  Args:
      numbers: A list of numbers.

  Returns:
      The unique number in the list.
  """
  # Count the occurrences of each number
  counts = {}
  for num in numbers:
    counts[num] = counts.get(num, 0) + 1

  # Find the number with a count of 1 (the unique number)
  for num, count in counts.items():
    if count == 1:
      return num

# Examples
print(unique([3, 3, 3, 7, 3, 3]))  # Output: 7
print(unique([0, 0, 0.77, 0, 0]))  # Output: 0.77
print(unique([0, 1, 1, 1, 1, 1, 1, 1]))  # Output: 0
