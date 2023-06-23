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

 
print('Welcome to Petes Tattoo Shop', 'what\'s your name?')

cust1 = Customer()

#print("Here are the Artists today, please choose one.")

names = []
for person in artists:
    names = []
    names.append(list(artists.keys()))

print(names)


#if 'mean' in user_input:
  #  print(artists['John'])
#elif user_input == 'so-so':
   # print(artists['Kerry'])
#else:
   # print('You did not choose anyone but here are you options:', artists.())


