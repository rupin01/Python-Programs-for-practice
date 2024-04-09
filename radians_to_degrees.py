import math
def radians_to_degrees(radians):
 degrees = radians * (180 / math.pi)
 return round(degrees, 1)

# Test cases
print(radians_to_degrees(1))
print(radians_to_degrees(20))
print(radians_to_degrees(50))
