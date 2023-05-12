# Program that takes Input
start_alpha = input('Enter alphabet you want to start with:   ')
end_alpha = input('Enter alphabet you want to end with:   ')
parameter1 = ord(start_alpha)
parameter2 = ord(end_alpha)

alpha_dict = {}
for i in range(parameter1, parameter2+1):
    alpha_dict[chr(i)] = i

print(alpha_dict)


# Without input the whole dictionary
# alpha_dict = {}
# for i in range(97, 123):       # Asci values directly hard-coded
#     alpha_dict[chr(i)] = i

# print(alpha_dict)
#
#
# Same program with functions
# def inp_func():
#     start_alpha = input('Enter alphabet you want to start with:   ')
#     end_alpha = input('Enter alphabet you want to end with:   ')
#     parameter1 = ord(start_alpha)
#     parameter2 = ord(end_alpha)
#     return parameter1, parameter2

# def Dictionary_func():
#     val1, val2 = inp_func()
#     alpha_dict = {}
#     for i in range(val1, val2+1):
#         alpha_dict[chr(i)] = i

#     return alpha_dict

# print(Dictionary_func)
