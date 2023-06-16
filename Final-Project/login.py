import re
import json
import os



# Please change file path here
existence = os.path.exists(r'D:\Edyoda\FOOD DELIVERY APP\users.json')
if existence == False:
    with open(r'D:\Edyoda\FOOD DELIVERY APP\users.json', 'w') as file:
        json.dump({"ADMIN":{}, "USER":{}}, file)

class Login:


    def user_type(self):
        user_is_a = input('\nPress any key if you are a USER otherwise enter the secret code to register as a ADMIN:   ')
        identity = 'ADMIN' if user_is_a == '123456' else 'USER'
        return identity

    def user_data(self):
        # Please change file path here
        with open(r'D:\Edyoda\FOOD DELIVERY APP\users.json') as file:
            user_pass = json.load(file)
        return user_pass


    def Start_func(self):

        while True:
            choice = input('\nPress 1 for Login and 2 for Registration and 3 to exit:  ')
            if choice == '1':
                self.login()
                break
            elif choice == '2':
                self.registrtion()
                break
            elif choice == '3':
                print("Exited login/registration page")
                exit(1)
                break
            else:
                print('Invalid input, Please try again!')

    def login(self):
        identity = self.user_type()
        user_pass = self.user_data()
        user_inp = input('\nEnter your username:   ')
        if user_inp in user_pass[identity]:
            while True:
                pass_inp = input('Enter your paswword:    ')
                if identity == 'ADMIN' and pass_inp == user_pass[identity][user_inp]:
                    print(f'You have logged in succesfully as a {identity}')
                    self.__authority = identity
                    self.__current_user = user_inp
                    break
                elif identity == 'USER' and pass_inp == user_pass[identity][user_inp]["password"]:
                    print(f'You have logged in succesfully as a {identity}')
                    self.__authority = identity
                    self.__current_user = user_inp
                    break
                else:
                    print('Passwoord is incorrect, pls try again')
        else:
            print("User does not exist, Do you wish to register")

            while True:
                y_n = input('Enetr "y" for yes and "n" for no:'    )
                if y_n == 'y':
                    self.registrtion()
                    break
                elif y_n == 'n':
                    print('No problem')
                    self.__authority = None
                    break
                else:
                    print('Invalid Input, please try agian')
    
    def get_identity(self):
        return self.__authority
    
    def get_username(self):
        return self.__current_user

        

    def registrtion(self):
        identity = self.user_type()
        user_pass = self.user_data()
        username = input('Enter your username:   ')
        if username in user_pass[identity]:
            print('Username already exists, Please use another')
            self.registrtion()
        else:
            while True:
                password = input('Enter your paswword:    ')
                pattern = r'\A(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!])(?!.*\s).{8,16}\Z'
                if re.findall(pattern, password):
                    if identity == 'USER':
                        fullname = input('Enter your Full Nmae:  ')
                        phoneno = input('Enter your Phone Number:  ')
                        email = input('Enter your E-mail ID:  ')
                        address = input('Enter your address:  ')
                        password = {"password":password, "full_name":fullname, "phone_no":phoneno, "email":email, "address":address}
                    user_pass[identity][username] = password
                    # Please change file path here
                    with open(r'D:\Edyoda\FOOD DELIVERY APP\users.json', 'w') as f:
                        json.dump(user_pass, f)
                    print(f'Registration Successfull! you are a {identity} now')
                    break
                else:
                    print('Password does not match the conditions, Try again')
            self.Start_func()

    def Update_Profile(self):
        if self.__authority == 'USER':
            user_pass = self.user_data()
            attribut_tup = ("full_name", "phone_no", "email", "address", "password")
            while True:
                choice = int(input('''\nWhat do you want to Update?
                1. Full Name
                2. Phone Number
                3. Email
                4. Address
                5. Password
                6.I am done changing, Please exit:   '''))
                if choice<6:
                    user_pass[self.__authority][self.__current_user][attribut_tup[choice-1]] = input(f'Enter your updated {attribut_tup[choice-1]}:  ')
                else:
                    # Please change file path here
                    with open(r'D:\Edyoda\FOOD DELIVERY APP\users.json', 'w') as f:
                        json.dump(user_pass, f)
                    break


# loginobj = Login()
# loginobj.Start_func()
# print(loginobj.authority, loginobj.current_user)
# loginobj.Update_Profile()