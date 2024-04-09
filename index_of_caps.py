def index_of_caps(word):
 # Use list comprehension to find indices of capital letters
 return [i for i, char in enumerate(word) if char.isupper()]
print(index_of_caps("eDeBiT"))
print(index_of_caps("eQuINoX"))
print(index_of_caps("determeine"))
print(index_of_caps("STRIKE"))
print(index_of_caps("sUm"))