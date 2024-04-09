def triangle(n):
    if n<1:
        return 0
    return n*(n+1)//2
print(triangle(2))
print(triangle(6))
print(triangle(215))