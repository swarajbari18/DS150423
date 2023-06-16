class LoginError(Exception):
    def __str__(self):
        return "The Login was Un-Succesfull, Please Try Again!"



class WrongChoiceError(Exception):
    def __str__(self):
        return "Input you gave is not in the choices given"
    

class EmptyMenuError(Exception):
    def __str__(self):
        return "The Admin has not entered anything in the menu, please contact the admin"