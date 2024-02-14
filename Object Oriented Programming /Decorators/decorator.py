
def my_deco(func):
    def mywork():
        print("\nHellow, Great Morning....! ")
        func()
        print("Finally, My work has been done.")
    return mywork

@my_deco
def my_math():
    x, y = [int(i) for i in input("Enter Two Number For Operation : ").split()]
    print("Addition is : ", x+y)
    print(x*y, " ->> This is Multiplication")

@my_deco
def hello():
    print("I am a simple boy   :) ")

hello()
my_math()
