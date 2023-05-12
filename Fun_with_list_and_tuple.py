list_required = []
while True:
    print('\nDo you want to create a list of tuple OR add more tuples to your list\n')
    print('If YES enter "y", If NO enter "n"')
    y_n = input('\nEnter your response:    ',)
    if y_n == 'y':
        no1 = int(input('\nEnter your first number:    '))
        no2 = int(input('Enter your second number:    '))
        list_required.append((no1, no2))
    elif y_n == 'n':
        break
    else:
        print('\nINVALID INPUT, TRY AGAIN')

print(f'Orignal List you have created(Sample Input):  {list_required}')

for i in range(len(list_required)):
    for j in range(i+1, len(list_required)):
        if list_required[i][1]>list_required[j][1]:
            list_required[i], list_required[j] = list_required[j], list_required[i]

print(f'Sorted list according to conditions(Expected Result):   {list_required}')