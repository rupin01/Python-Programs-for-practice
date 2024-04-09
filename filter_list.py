def filter_list(l):

  return [item for item in l if isinstance(item, int)]

# Examples
print(filter_list([1, 2, "a", "b"]))  # Output: [1, 2]
print(filter_list([1, "a", "b", 0, 15]))  # Output: [1, 0, 15]
print(filter_list([1, 2, "aasf", "1", "123", 123]))  # Output: [1, 2, 123]