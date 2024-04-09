def setify(lst):
 unique_set = set(sorted(lst))

 # Convert the set back to a list and return it
 return list(unique_set)

print(setify([1, 3, 3, 5, 5]))
print(setify([4, 4, 4, 4]))
print(setify([5, 7, 8, 9, 10, 15]))
print(setify([3,3,3,2,1]))