def vow_replace(text, vowel):
  """
  Replaces all vowels in a string with a specified vowel.

  Args:
      text: The input string.
      vowel: The vowel to replace other vowels with.

  Returns:
      The modified string with replaced vowels.
  """
  # Create a translation table to map vowels to the new vowel
  vowels = "aeiou"
  translation = str.maketrans(vowels, vowel * len(vowels))

  # Translate the text using the translation table
  return text.translate(translation)

# Examples
print(vow_replace("apples and bananas", "u"))  # Output: "upplus und bununus"
print(vow_replace("cheese casserole", "o"))  # Output: "chooso cossorolo"
print(vow_replace("stuffed jalapeno poppers", "e"))  # Output: "steffed jelepene peppers"
