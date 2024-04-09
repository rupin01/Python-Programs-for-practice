def is_in_order(s):

 return s == ''.join(sorted(s))

print(is_in_order("abc"))
print(is_in_order("edabit"))
print(is_in_order("123"))
print(is_in_order("xyzz"))