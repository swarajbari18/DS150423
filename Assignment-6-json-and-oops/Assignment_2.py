class Dog:
    def __init__(self, name, age, coat_colour):
        self.name = name
        self.age = age
        self.coat_colour = coat_colour

    def description(self):
        print(f'''
              Name:  {self.name}
              Age:   {self.age}''')
        
    def get_info(self):
        print(f'His coat colour is {self.coat_colour}')


class JackRussellTerrier(Dog):
    def strength(self):
        return 'Very strong'
    
    def speed(self):
        return '40 kmph'

class Bulldog(Dog):
    def sense_of_smell(self):
        return 'Very high'
    
    def aggresion(self):
        return 'Highly Aggressive'
    

obj1 = JackRussellTerrier('Tommy', 29, 'Brown')
obj2 = Bulldog('Bully', 13, 'white')

obj1.description()
obj1.get_info()
obj2.description()
obj2.get_info()
strength = obj1.strength()
speed = obj1.speed()
smell = obj2.sense_of_smell()
anger = obj2.aggresion()

print(f'\n{strength}\n{speed}\n{smell}\n{anger}')