######################################## TASK 1 #############################################################################################################


import json
with open(r'D:\Edyoda\Assignment_6_json&oops\employee.json') as file1:
    data = json.load(file1)

# print(data)

class Employee:
    def __init__(self, data1):
        self.name = data1["Name"]
        self.dob = data1["DOB"]
        self.hieght = data1["Hieght"]
        self.city = data1["City"]
        self.state = data1["State"]

    # The assignment did not say to make a __str__ method, but I made this to check weather the 
    # objects were correctly formed or not,mam you may also check that by unhashing the last two lines of code.

    def __str__(self):
        return f'{self.name} born on {self.dob} is {self.hieght} tall and lives in {self.city}, {self.state}'

def write_to_list_func():
    employee_list = []
    for i in data:
        employee_object = Employee(data[i])
        employee_list.append(employee_object)
    return employee_list

list_of_objects = write_to_list_func()
print('\nList of all the Employee class objects :         ', list_of_objects)



#please unhash the below code to check weather the objects are formed correctly or not
# they should print thier own __str__ methods 

# for object in list_of_objects:
#     print('\n',object)







######################################################  TASK 2  #########################################################################################

states_and_capitals = {"Maharashtra":"Mumbai",
                       "Telangana":"Hyderabad",
                       "Tamilnadu":"Chennai",
                       "Karnataka":"Bengaluru",
                       "Bihar":"Patna",
                       "Rajasthan":"Jaipur", 
                       "Gujrat":"Gandhinagar"}


with open(r'D:\Edyoda\Assignment_6_json&oops\Indian_state_and_capital.json', 'w') as file2:
    json.dump(states_and_capitals, file2)




