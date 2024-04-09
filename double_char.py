def double_char(input_str):
    doubled_str=" "

    for char in input_str:
        doubled_str+=char*2

    return doubled_str
print(double_char("String"))
print(double_char("Hello World"))
print(double_char("1234!_"))