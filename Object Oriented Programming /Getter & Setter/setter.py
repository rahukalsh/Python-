class YourBank:
    def __init__(self, bal):
        self.balance = bal

    def work(self):
        print(f"This is your {self.balance} Rs.")
    
    @property
    def upto(self):
        print(f"Your bal is : {self.balance}")
        return 2 * self.balance

    @upto.setter
    def uptodate(self, new_val):
        self.balance = new_val - 11

cust = YourBank(210)
cust.work()
print(cust.upto)
cust.work()
cust.uptodate = 55              # Now we can change actual value or set/change attributes.
print(cust.uptodate)
cust.work()
