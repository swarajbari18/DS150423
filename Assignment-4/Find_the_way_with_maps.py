sample_lst = [1, 2, 3, 4, 5, 6, 7]

# Creating a list by user input
# sample_lst = []
# input_length = int(input('Enter the length of list you need:   '))
# for j in range(input_length):
#     input_value = float(input('Enter values of the list in corresponding lines:  '))
#     sample_lst.append(input_value)

sample_output = list(map(lambda x : 3*x, sample_lst))
print(f'Sample input: {sample_lst}\nSample output: {sample_output}')