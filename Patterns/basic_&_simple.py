
# --------  Increasing Left to Right ---------

num = int(input("Enter a number for Pattern : \n"))
for i in range(num):
    for j in range(i+1):
        print("*", end=" ")
    print('')

# -------- Decreasing Right to Left ---------

num = int(input("Enter a number for Pattern : \n"))
for i in range(num):
    for j in range(i,num):
        print("*", end=" ")
    print('')

# -------- Increasing Right to Left ---------

num = int(input("Enter a number for Pattern : \n"))
for i in range(num):
    for j  in range(i,num-1):
        print(' ',end=' ')
    for j in range(i+1):
        print('*', end=' ')
    print("")

# --------  Decreasing Left to Right ---------

num = int(input("Enter a number for Pattern : \n"))
for i in range(num):
    for j in range(i):
        print(" ", end=' ')
    for j in range(i,num):
        print("*", end=' ')
    print('')
