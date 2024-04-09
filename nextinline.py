def next_in_line(lst, num):
   if lst:
     lst.pop(0) # Remove the first element
     lst.append(num) # Add the number to the end
     return lst
   else:
     return "No list has been selected"
   
print(next_in_line([5, 6, 7, 8, 9], 1))
print(next_in_line([7, 6, 3, 23, 17], 10))
print(next_in_line([1, 10, 20, 42 ], 6))
print(next_in_line([], 6))