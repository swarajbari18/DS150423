class Student:
    #setters
    def setName(self):
        name = input('Enter the name of student:  ')
        self.__name = name
    def setRollNumber(self):
        rollno = int(input('Enter your roll no: '))
        self.__rollNumber = rollno
    #getters
    def getName(self):
        return self.__name
    def getRollNumber(self):
        return self.__rollNumber

#Must not pass any aruguments into the setters.
student1 = Student()
student1.setName()
student1.setRollNumber()
name_got = student1.getName()
rollno_got = student1.getRollNumber()
print(f'Name is {name_got} and roll no is {rollno_got}.')
