#------------  Hybrid Inheritance ---------------------

class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def show_details(self):
    print("\nName:", self.name)
    print("Age:", self.age)
    
class Person(Human):
  def __init__(self, name, age, address):
    Human.__init__(self, name, age)
    self.address = address
    
  def show_details(self):
    Human.show_details(self)
    print("Address:", self.address)
    
class Program:
  def __init__(self, program_name, duration):
    self.program_name = program_name
    self.duration = duration
    
  def show_details(self):
    print("Program Name:", self.program_name)
    print("Duration:", self.duration," Years")
    
class Student(Person):
  def __init__(self, name, age, address, program):
    Person.__init__(self, name, age, address)
    self.program = program
    
  def show_details(self):
    Person.show_details(self)
    self.program.show_details()

cs_course = Program("Computer Science Engineering", 4)
student_1 = Student("Johnethon Deo", 25, "123 Main St. Bleziam", cs_course)

mba_course = Program("Master's in Business Administrator", 2)
student_2 = Student("Robert Charlee ", 31, "Colt Road, 494 St. Venezuala ", mba_course)

student_1.show_details()
student_2.show_details()
