def replace_vowels(string,char):
    vowels="aeiouAEIOU"
    new_string=" "
    for letter in string:
        if letter in vowels:
            new_string+=char
        else:
            new_string+=letter
    return new_string

print(replace_vowels("the aardvark", "#"))
print(replace_vowels("minnie mouse", "?"))
print(replace_vowels("shakespeare", "*"))