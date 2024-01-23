''' 
    Fabonacci Series is the sum of past two numbers.
    Examples :  
               f(0) = 0         f(1) = 1        f(2) = 1
              
               f(3) = 2        f(4) = 3        f(5) = 5
              
        f(n) = f(n-1) + f(n-2)               

'''

def fabonacci(n):
    if n <= 1 :
        return n
    else:
        return (fabonacci(n-1) + fabonacci(n-2))    

feb_list = []
num = int(input(" Enter your number for Fabonacci Series : "))
if num < 0 :
    print("Please Enter a Valid Positive Number !!!")
else:
    for i in range(num+1):
        feb_list.append(fabonacci(i))
print(f'\nFabonacci Series is :\n\n{feb_list}')        
