def ascii_capitalize(text):
  """Capitalizes a letter if its ASCII code is even and returns its lower case version if its odd.

  Args:
      text: The text to be transformed.

  Returns:
      The transformed text.
  """
  return ''.join(c.upper() if ord(c) % 2 == 0 else c.lower() for c in text)

# Examples
print(ascii_capitalize("to be or not to be!"))  # Output: To Be oR NoT To Be!
print(ascii_capitalize("THE LITTLE MERMAID"))  # Output: THe LiTTLe meRmaiD
print(ascii_capitalize("Oh what a beautiful morning."))  # Output: oH wHaT a BeauTiFuL moRNiNg.
