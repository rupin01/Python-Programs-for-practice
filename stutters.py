def stutter(word):
    if len(word)<2:
        return "Word must be at least two characters long"
    
    stuttered_word=f"{word[:2]}...{word[:2]}...{word}?"
    return stuttered_word

print(stutter("incredible")) 
print(stutter("enthusiastic")) 
print(stutter("outstanding"))