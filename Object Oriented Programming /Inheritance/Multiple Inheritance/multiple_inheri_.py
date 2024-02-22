#------------  Multiple Inheritance ---------------------

class Employee:
    def __init__(self,id, name):
        self.id = id 
        self.name = name
    def person_detail(self):
        print(f" ID No. - {self.id} \n Name : {self.name}")
    
class Banking:
    def __init__(self, ac_no, salary):
        self.ac_no = ac_no
        self.salary = salary 
    def bank_detail(self):
        print(f" The salary of {self.ac_no} A/C Holder is {self.salary} Rs.")

class Company(Employee, Banking):
    def __init__(self, name, id, ac_no, salary):
        Banking.__init__(self, ac_no, salary)
        Employee.__init__(self,id, name)
    def bank_info(self):
        print(f"\nYou are seeing bank details of {self.name} ")
        Banking.bank_detail(self)
    def person_info(self):
        print(f"\nThis is about our employee having A/C No. {self.ac_no}")
        Employee.person_detail(self)

emp_1 = Company("Shradha Didi", 101, "540xxxx96", "80K")
emp_2 = Company("Rounak Shingh", 202, "708xxxx38", "57K")
emp_3 = Company("Dhatarwal Ji", 303, "824xxxx21", "92K")

emp_2.bank_info()
emp_2.person_info()

emp_1.person_info()
emp_1.bank_info()

emp_3.bank_info()
emp_3.person_info()

#-----------------  Method Resolution Order (MRO) ---------------------
# it denotes the way a programming language resolves a method or attribute (means shows/finds the order of which class method executes first)

print(Company.__mro__)           # Output returns in Tuple
print(Company.mro())             # Output returns in List

