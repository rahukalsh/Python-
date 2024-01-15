with open("log.txt", "r") as f:
    match = f.readline()
    for i in range(1, 16):                      # Only has a limit to search 15 lines.
        if("python" in match):
            print(f'\nThis {i}th line contain the word "Python"\n')
            print(f'And the line is : {match}')
        match = f.readline()


##   This program is case sensitive. So 'Python' and 'python' is not same !!!