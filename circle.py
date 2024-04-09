import math

class Circle:
  """
  Represents a circle with a radius.
  """
  def __init__(self, radius):
    """
    Initializes a circle object.

    Args:
        radius: The radius of the circle.
    """
    self.radius = radius

  def getArea(self):
    """
    Calculates and returns the area of the circle.

    Returns:
        The area of the circle (PI * r^2).
    """
    return round(math.pi * self.radius**2, 0)

  def getPerimeter(self):
    """
    Calculates and returns the perimeter of the circle.

    Returns:
        The perimeter of the circle (2 * PI * r).
    """
    return round(2 * math.pi * self.radius, 0)

# Examples
circy = Circle(11)
print(circy.getArea())  # Output: 380
print(circy.getPerimeter())  # Output: 69

tiny_circle = Circle(4.44)
print(tiny_circle.getArea())  # Output: 62
print(tiny_circle.getPerimeter())  # Output: 28
