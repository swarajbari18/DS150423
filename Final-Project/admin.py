import json
import os


# Please change file path here
existence = os.path.exists(r'D:\Edyoda\FOOD DELIVERY APP\MENU.json')
if existence == False:
    with open(r'D:\Edyoda\FOOD DELIVERY APP\MENU.json', 'w') as file:
        json.dump({}, file)


class Admin:

    # Please change file path here
    with open(r'D:\Edyoda\FOOD DELIVERY APP\MENU.json') as file:
        menu = json.load(file)

    def update_menu(self):
        # Please change file path here
        with open(r'D:\Edyoda\FOOD DELIVERY APP\MENU.json', 'w') as file1:
            json.dump(self.menu, file1)        

    def add_Food(self):
        self.FoodID = len(self.menu)+1
        print(f'\nFoodId:  {self.FoodID}')
        self.name = input('Enter Food Name:  ')
        self.quantity = input('Enter Quantity (please specify units):  ')
        self.price = input('Enter Price:  ')
        self.discount = input('Enter Discount:  ')
        self.stock = input('Enter stock remaining:  ')
        self.menu[self.FoodID] = {"name":self.name, "quantity":self.quantity, "price":self.price, "discount":self.discount, "stock":self.stock}
        self.update_menu()

    def edit_food(self):
        id = int(input('Enter FoodID:  '))
        attributr_tup = ('name', 'quantity', 'price', 'discount', 'stock')
        if id in self.menu:
            while True:
                choice = int(input('''What do you want to change?
                1. name
                2. quantity
                3. price
                4. discount
                5. stock
                6.I am done changing, Please exit:   '''))
                if choice<6:
                    self.menu[id][attributr_tup[choice-1]] = input(f'Enter your updated {attributr_tup[choice-1]}:  ')
                else:
                    self.update_menu()
                    break

        else:
            print('This Food id does not exist')

    def view_menu(self):
        print('\t\t\tMENU')
        for k, v in self.menu.items():
            print(f'''
            
            
            {k}
            {v['name'].upper()}
            {v['quantity']}
            {v['price']+' Rupees only with GST'}
            {v['discount']}
            {v['stock']}''')

    def delete_food(self):
        id = int(input('Enter FoodID:  '))
        if id in self.menu:
            self.menu.pop(id)
            self.update_menu()
        else:
            print('This Food id does not exist')



# adminobj = Admin()
# adminobj.view_menu()
# adminobj.add_Food()
# adminobj.add_Food()
# adminobj.edit_food()
# adminobj.edit_food()
# adminobj.view_menu()
# adminobj.delete_food()
# adminobj.view_menu()