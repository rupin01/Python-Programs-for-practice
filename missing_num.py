def missing_num(lst):
    total_num=sum(range(1,11))
    given_sum=sum(lst)
    missing=total_num-given_sum
    return missing

print(missing_num([1,2,3,4,5,6,7,8,9,10]))
print(missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]))
print(missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]))