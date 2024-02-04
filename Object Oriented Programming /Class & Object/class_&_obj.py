# Class defining 
class Profile:
    name = "Your Namre"
    occup = "Occupation is"
    salary = "How Much"

    # Method creation
    def info(self):             
        print(f'{self.name} is a good {self.occup} and get salary of {self.salary} PM.')

# Object define 
user1 = Profile()
user2 = Profile()
user3 = Profile()

user1.name = "Rahul"
user1.salary = "84 K"
user2.occup = "DevOps Engg."
user2.salary = "134 K"
user3.occup = "Gov. Teacher"
user3.name = "Sandeep"

print(user1.occup, user3.name, user2.salary)
user1.info()
user2.info()
user3.info()
