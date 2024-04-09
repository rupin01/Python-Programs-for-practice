def sort_by_length(lst):
    return sorted(lst, key=len)
print(sort_by_length(["Google", "Apple", "Microsoft"]))
print(sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"]))
print(sort_by_length(["Turing", "Einstein", "Jung"]))