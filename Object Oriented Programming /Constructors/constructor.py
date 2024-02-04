# Class defining 
class Profile:

    # This is constructor (every time automatically call when a object create, means 5 object created then 5 times called)
    def __init__(self, person, passion, pay):
        self.name = person                      # We can also use self.name = name 
        self.occu = passion                     # We can also use self.occu = occu
        self.salary = pay                       # We can also use self.salary = salary
        
        print("Is it print everytimes")         # Yes it print everytime when object created 

    # Method creation
    def info(self):             
        print(f'{self.name} is a good {self.occu} and get salary of {self.salary} PM.')

# Object define 
user1 = Profile("Rahul", "Computer Engg.", "Approx 73 K")
user2 = Profile("Divya", "HR Depart.", "Minimum 56 K")
user3 = Profile("Suraj", "Artist", "Approx 42 K")


print(user1.occu, user3.name, user2.salary)
user1.info()
user2.info()
user3.info()

