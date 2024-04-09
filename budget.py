def get_budgets(lst):
 total_budget = sum(person['budget'] for person in lst)
 return total_budget
# Test cases
budgets1 = [
 {'name': 'John', 'age': 21, 'budget': 23000},
 {'name': 'Steve', 'age': 32, 'budget': 40000},
 {'name': 'Martin', 'age': 16, 'budget': 2700}
]
budgets2 = [
 {'name': 'John', 'age': 21, 'budget': 29000},
 {'name': 'Steve', 'age': 32, 'budget': 32000},
 {'name': 'Martin', 'age': 16, 'budget': 1600}
]

print(get_budgets(budgets1))
print(get_budgets(budgets2))