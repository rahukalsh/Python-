class YourBank:
    def __init__(self, bal):
        self.balance = bal

    def work(self):
        print(f"This is your {self.balance} Rs.")
    
    @property
    def upto(self):
        print(f"Your bal is : {self.balance}")
        return self.balance + 11


cust = YourBank(500)
cust.work()
print(cust.upto)      # Does not change actual value. Just act as object's property.
cust.work()
