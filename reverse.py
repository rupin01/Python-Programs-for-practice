def reverse(s):

  # Swap case and reverse the string
  return s[::-1].swapcase()

# Examples
print(reverse("Hello World"))  # Output: "DLROw OLLEh"
print(reverse("ReVeRsE"))  # Output: "eSrEvEr"
print(reverse("Radar"))  # Output: "RADAr"
