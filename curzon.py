def is_curzon(num):
 numerator = 2 ** num + 1
 denominator = 2 * num + 1
 return numerator % denominator == 0
# Test cases
print(is_curzon(5)) 
print(is_curzon(10)) 
print(is_curzon(14)) 