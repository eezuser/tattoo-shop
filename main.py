artists = {'John':['mean', 2], 'Kerry': ['so-so', 1], 'Josh': ['nice', 10]}


class Customer:
    def __init__(self, attitude):
        self.attitude = attitude

    def get_attitude(self):
        return self.attitude
    
class Artist:
    def __init__(self, attitude, level, name):

        self.attitude = attitude
        self.level = level 
        self.name = name  
    
user_input = input(str('What artist would you like today?'))

if 'mean' in user_input:
    print(artists['John'])
elif user_input == 'so-so':
    print(artists['Kerry'])
else:
    print(artists.keys())


