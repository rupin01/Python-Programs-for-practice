def find_duplicates(string):
  """
  Finds all duplicate characters in a string.

  Args:
      string: The string to search for duplicates.

  Returns:
      A set containing all duplicate characters in the string.
  """
  char_counts = {}
  duplicates = set()
  for char in string:
    if char in char_counts:
      duplicates.add(char)
    else:
      char_counts[char] = 1
  return duplicates

# Example usage
string = "Piyush Sharma"
duplicates = find_duplicates(string)

if duplicates:
  print("Duplicate characters:", duplicates)
else:
  print("No duplicate characters found.")
