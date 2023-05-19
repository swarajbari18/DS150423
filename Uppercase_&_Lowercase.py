def calculate_case(some_string):
    lower_case = 0
    upper_case = 0
    for i in some_string:
        if i.isupper():
            upper_case += 1
        elif i.islower():
            lower_case += 1
    
    return lower_case, upper_case


string_input = input('Enter your string:    ')
lower_no, upper_no = calculate_case(string_input)
print(f'\nNo. of Upper case characters are:  {upper_no}.\nNo. of lower case characters are:  {lower_no}')