input_lst = []
condition = True
while condition is True:
    if condition is True:
        n = int(input('Enter your number ===> '))
        input_lst.append(n)
        print('\nDo you Want to add another number to your number Group\n ')
        print("""If YES then press "Enter" """)
        print("""If NO then "Press any key and then hit enter"\n """)
        y_n = input('Enter your respponse ===> ')
        if y_n == '':
            condition = True
        else :
            condition = False
    else:
        break

print('\nYou Entered number Group is :  ', input_lst, '\n')

even_no = 0
odd_no = 0
for i in input_lst:
    if i%2 == 0:
        even_no += 1
    else:
        odd_no += 1
print('Number of even numbers:  ', even_no)
print('Number of odd numbers:   ', odd_no)