class Casting:
    def __init__(self, reel_name, hero_name):
        self.reel_name = reel_name
        self.hero_name = hero_name
    def show(self):
        print(f"This is Character Name : {self.reel_name}")
        print(f"This is Our Hero Name : {self.hero_name}\n")

class Movie(Casting):
    def __init__(self,real_name, reel_name, hero_name):
        self.real_name = real_name  
        #------------  Callling Constructor (__init__) of the Parent Class  --------------                     
        Casting.__init__(self, reel_name, hero_name)        
    def details(self):
        print(f"The Real name of Character is : {self.real_name}")
        print("Names in the Marvel's Movie ")
        super().show()
    
obj = Movie("RDJ", "Tony Stark", "Iron Man")
obj.details()
obj.show()
