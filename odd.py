#sample list of numbers
numbers=[1,2,3,4,5,6,7,8,9,10]

#using a list comprehension to filter even numbers
odd_numbers=[num for num in numbers if num%2 !=0]

#Print the en=ven numbers
print("Odd numbers in the list:",odd_numbers)