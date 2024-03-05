#------------  Hierarchical Inheritance ---------------------

class Details:
    def __init__(self, id, name):
        self.id = id 
        self.name = name
    
    def get_details(self):
        print("ID :", self.id)
        print("Name :", self.name)

class Docter(Details):
    def __init__(self, id, name, hospital, disease):
        Details.__init__(self, id, name)
        self.hospital = hospital
        self.department = disease
    
    def show_detail(self):
        print("\n\t ------- This is Doctor's Object ---------")
        Details.get_details(self)
        print("Hospital Name :", self.hospital)
        print("Disease is :", self.department)

class Employee(Details):
    def __init__(self, id, name, company, deparment):
        Details.__init__(self, id, name)
        self.company = company
        self.work = deparment

    def show_detail(self):
        print("\n\t ------- This is Company's Object ---------")
        Details.get_details(self)
        print("Company Name :", self.company)
        print("Department is :", self.work)
    
patient_1 = Docter(101, "Gourav Shah", "AIIMS Kanpur", "Influenza (flu)")
patient_1.show_detail()

person_1 = Employee(202, "Sourabh Gupta", "IndoCast Ltd.", "Sr. Machine Oprator")
person_1.show_detail()
