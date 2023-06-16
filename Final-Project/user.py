import json
import os
from Errors import EmptyMenuError


# Please change file path here
existence = os.path.exists(r'D:\Edyoda\FOOD DELIVERY APP\MENU.json')
if existence == False:
    raise Exception


class Users:


    # Please change file path here
    with open(r'D:\Edyoda\FOOD DELIVERY APP\MENU.json') as file:
        menu = json.load(file)

    
    def view_menu(self):
        print('\t\t\tMENU')
        if self.menu == {}:
            raise EmptyMenuError()
        for k, v in self.menu.items():
            print(f"\n{k}. {v['name']} ({v['quantity']}) [{v['price']}]")

    def place_a_order(self):
        self.view_menu()
        order = input('Enter your order id from the menu, sperated by space:  ')
        order_array = order.strip().split(' ')
        print('Selected Items Are: ')
        allorders = ''
        for i in order_array:
            allorders += f'{self.menu[i]["name"]} ({self.menu[i]["quantity"]}) [{self.menu[i]["price"]}]\n'
        print(allorders)
        print('Do you wish to place this order ')
        y_n = input('Enetr "y" for yes and "n" for no:'    )
        if y_n == 'y':
            print('You have succesfully placed your order!')

        else:
            print('No problem')
        return allorders
        
