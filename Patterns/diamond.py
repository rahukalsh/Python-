# --------  Diamond Pattern  -------

num3 = int(input("Length of the Dimond ? => "))
print("\n")
for i in range(num3-1):
    for j in range(i+1,num3):
        print(' ', end=' ')
    for j in range(i+1):
        print('*', end=' ')
    for j in range(i):
        print("*", end=" ")
    print('')

for i in range(num3):
    for j in range(i):
        print(" ", end=' ')
    for j in range(i,num3):
        print("*", end=' ')
    for j in range(i,num3-1):
        print("*", end=' ')
    print('')
print("\n")
