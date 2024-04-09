#sort the keys:

sample_dict={'apple':3,'banana':1,'cherry':2,'date':4}

sorted_dict_by_keys=dict(sorted(sample_dict.items()))
print("Sorted by keys:")
for key,value in sorted_dict_by_keys.items():
    print(f"{key}: {value}")


#Sort by Values:
# Python code demonstrate the working of
# sorted() with lambda

# Initializing list of dictionaries
list = [{"name": "Rupin", "age": 23},
	{"name": "Jaspreet", "age": 29},
	{"name": "Riya", "age": 22}]

# using sorted and lambda to print list sorted
# by age
print("The list printed sorting by age: ")
print(sorted(list, key=lambda i: i['age']))

print("\r")

print("The list printed sorting by age and name: ")
print(sorted(list, key=lambda i: (i['age'], i['name'])))

print("\r")

# using sorted and lambda to print list sorted
# by age in descending order
print("The list printed sorting by age in descending order: ")
print(sorted(list, key=lambda i: i['age'], reverse=True))