# ----------  I think this Pattern is looks like a Home !!!  --------

num1 = 8
for i in range(num1):
    for j in range(i+1,num1):
        print(" ", end=' ')
    for j in range(i+1):
        print("❄", end=' ')
    for j in range(i):
        print("❄", end=' ')
    print('')

num2 = 10
for i in range(num2):
    for j in range(num2):
        if(i==0 or j==0 or i==num2-1 or j==num2-1):
            print("🧱", end='')
        else:
            print("  ", end=' ')
    print('')
