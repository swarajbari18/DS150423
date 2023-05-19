def str_reverse_func(some_string):
    return some_string[::-1]

# A more logic based approach for the same function is
# def str_reverse_func(some_string):
#     reverse = ''
#     for i in some_string:
#         reverse = i + reverse
#     return reverse

string_input = input('Enter your string:   ')
output = str_reverse_func(string_input)
print('The reverse of the given string is:  ', output)


