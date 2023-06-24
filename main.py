artists = {'John':['mean', 2], 'Kerry': ['so-so', 1], 'Josh': ['nice', 10]}

# Customer class
class Customer:
    def __init__(self):
       self.name = input('What is your name?\n')
       self.attitude = input('How is your attitude?\n')
        

  
#Artist class    
class Artist:
    def __init__(self, attitude, level, name):

        self.attitude = attitude
        self.level = level 
        self.name = name  

names = []
for person in artists:
    names = []
    names.append(list(artists.keys()))
 
print('Welcome to Pete\'s Tattoo Shop')
print('Here is a list of the Artists')
print(names)

cust1 = Customer()

if cust1.attitude == 'Bad' or 'mean' or 'bad' or 'Mean':
    lowest_skill = names[0][0]
    print( 'Alright', cust1.name, 'it looks like you have a', cust1.attitude, 'attitude, so', lowest_skill, 'will be your Artist today.')
elif cust1.attitude == 'good' or 'Good' or 'fine':
    good_skill = names[2][2]
    print("Gotcha covered,", good_skill, "is a good choice.")
else:
    medium_skill = names[1][2]
    print('Cant make a choice?, no worries', medium_skill, 'is a solid Artist.')






