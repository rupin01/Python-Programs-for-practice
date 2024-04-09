def is_isogram(word):
    word = word.lower()
    seen = set()
    for letter in word:
        if letter.isalpha():
            if letter in seen:
                return False
            seen.add(letter)
    return True

# Test cases
print(is_isogram("Algorism"))      # ➞ True
print(is_isogram("PasSword"))      # ➞ False
print(is_isogram("Consecutive"))    # ➞ False