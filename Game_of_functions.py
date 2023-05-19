def sum_func(list_para):
    sum = 0
    for i in list_para:
        sum += i
    return sum

#  Input Function
lst = []
input_length = int(input('Enter the length of list you need:   '))
for j in range(input_length):
    input_value = float(input('Enter values of the list in corresponding lines:  '))
    lst.append(input_value)
#  Sample Input ,Please unhash below lst if you wish to use the sample input as given in the question
# lst = [8, 2, 3, 0, 7]
result = sum_func(lst)
print(f'\nThe summation of all the numbers in the list is {result}\n')