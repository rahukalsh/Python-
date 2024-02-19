
# Base Class ( Parent )
class Manager:
    def __init__(self, name, id):
        self.name = name 
        self.id = id
        
    def work(self):
        print(f"\nThis is our {self.name} having  id {self.id} ")
        # print(f"Age is {age} years")      "___Error___" -->>  parent cann't have the access of child attributes 

# Derived Class ( Child )   
class Employee(Manager):       # Having all the Properties of parent Class ( Can Access parent's Attributes )

    def working(self, age):
        print(f"Age of the {self.name} is {age} years")
        print(f"And {self.name} ID is {self.id}\n")

paradox = Manager("akash", 1001)
paradox.work()
# paradox.working(19)   "__Error__"  -->>  Cann't allowance to access the derived class (Child) Methodes/properties 

person_1 = Employee("Subham", 101)
person_2 = Employee("Gaurav", 202)
person_3 = Employee("Hamzza", 303)

person_2.working(34)
person_2.work()
person_1.work()
person_1.working(27)
person_3.working(19)

print(person_1.id, person_3.name, person_2.id)
