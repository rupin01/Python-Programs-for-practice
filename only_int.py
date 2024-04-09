def return_only_integer(lst):
  """Returns a list containing only the integers from the input list.

  Args:
      lst: The list to process.

  Returns:
      A list containing only the integers from the input list.
  """
  return [i for i in lst if isinstance(i, int)]

# Examples
print(return_only_integer([9, 2, "space", "car", "lion", 16]))  # Output: [9, 2, 16]
print(return_only_integer(["hello", 81, "basketball", 123, "fox"]))  # Output: [81, 123]
print(return_only_integer([10, "121", 56, 20, "car", 3, "lion"]))  # Output: [10, 56, 20, 3]
print(return_only_integer(["String", True, 3.3, 1]))  # Output: [1]
