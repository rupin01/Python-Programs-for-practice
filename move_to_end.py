def move_to_end(lst,element):
    count=lst.count(element)

    lst=[x for x in lst if x != element]
    lst.extend([element]*count)

    return lst
print(move_to_end([1, 3, 2, 4, 4, 1], 1))
print(move_to_end([7, 8, 9, 1, 2, 3, 4], 9))
print(move_to_end(["a", "a", "a", "b"], "a") )