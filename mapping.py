def mapping(letters):
 result = {}
 for letter in letters:
   result[letter] = letter.upper()
 return result
print(mapping(["p", "s"]))
print(mapping(["a", "b", "c"]))
print(mapping(["a", "v", "y", "z"]))
