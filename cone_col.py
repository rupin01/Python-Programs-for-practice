import math
def cone_volume(height, radius):
 if radius == 0:
   return 0
 volume = (1/3) * math.pi * (radius**2) * height
 return round(volume, 2)

print(cone_volume(3, 2))
print(cone_volume(15, 6))