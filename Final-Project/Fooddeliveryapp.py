#Only run this file
# If you wish to register as admin,enter the secret code 123456 when it will ask you
#  You don't need to create any files, the code will do it by itself
# Please change the path of files in your system wherever i have mentioned it, in all five py files


from login import *
from admin import *
from user import *
from Errors import *
import datetime as dt

login_object = Login()
login_object.Start_func()
if login_object.get_identity() == 'ADMIN':
    admin_object = Admin()
    while True:
        print('''What do you wish yo do?
        
        1. Add new food items
        2. Edit existing food items
        3. View the food items
        4. Remove a food item
        5. Exit the program and go home''')
        action = input('Enter your action:  ')
        if action == '1':
            print('\n'+'* '*25+'Add Food Items'+'* '*25+'\n')
            admin_object.add_Food()
        elif action == '2':
            print('\n'+'* '*25+'Edit Food Items'+'* '*25+'\n')
            admin_object.edit_food()
        elif action == '3':
            print('\n'+'* '*25+'View Food Items'+'* '*25+'\n')
            admin_object.view_menu()
        elif action == '4':
            print('\n'+'* '*25+'Remove Food Items'+'* '*25+'\n')
            admin_object.delete_food
        elif action == '5':
            print('\nGOODBYE\n')
            break
        else:
            raise WrongChoiceError()


elif login_object.get_identity() == 'USER':
    user_object = Users()
    # Please change file path here
    file1 = open(f'D:\\Edyoda\\FOOD DELIVERY APP\\{login_object.get_username()}_order_history.txt', 'a')
    file1.close()
    while True:
        print('''What do you wish yo do?
            
            1. Place a Order! I am Hungry
            2. Order History
            3. Update Profile
            4. Exit the program and go home''')
        action = input('Enter your action:  ')
        if action == '1':
                print('\n'+'* '*25+'Food Ordering'+'* '*25+'\n')
                note_of_order = user_object.place_a_order()
                # Please change file path here
                with open(f'D:\\Edyoda\\FOOD DELIVERY APP\\{login_object.get_username()}_order_history.txt', 'a') as file2:
                    today_date = dt.datetime.now()
                    file2.write(f'{today_date}\n\n{note_of_order}')
        elif action == '2':
            print('\n'+'* '*25+'Order History'+'* '*25+'\n')
            # Please change file path here
            with open(f"D:\\Edyoda\\FOOD DELIVERY APP\\{login_object.get_username()}_order_history.txt") as file3:
                order_history = file3.read()
                print(order_history)
            
        elif action == '3':
            print('\n'+'* '*25+'Profile Update'+'* '*25+'\n')
            login_object.Update_Profile()
        elif action == '4':
            print('\nGOODBYE\n')
            break
        else:
            raise WrongChoiceError()
        
else:
    raise LoginError()



