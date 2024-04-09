def correct_signs(expression):
   try:
     return eval(expression)
   except:
     return False
print(correct_signs("3 < 7 < 11"))
print(correct_signs("13 > 44 > 33 < 1"))
print(correct_signs("1 < 2 < 6 < 9 > 3"))