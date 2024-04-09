limit = int(input("Enter the limit: "))
# Initialize the sum
sum = 0
# Use a for loop to calculate the sum of natural numbers
for i in range(1, limit + 1):
 sum += i
# Print the sum
print("The sum of natural numbers up to", limit, "is:", sum)