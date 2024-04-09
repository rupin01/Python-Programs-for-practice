def reverse(value):
    if isinstance(value,bool):
        return not value
    else:
        return "boolean expected"
    
print(reverse(True))
print(reverse(False))
print(reverse(0))
print(reverse(None))