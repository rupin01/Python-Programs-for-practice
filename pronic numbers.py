def is_pronic_number(num):
    for n in range(1,int(num**0.5)+1):
        return True
    return False
print("Pronic numbers between 1 and 100 are: ")
for i in range(1,100):
    if is_pronic_number(i):
        print(i, end=" | ")