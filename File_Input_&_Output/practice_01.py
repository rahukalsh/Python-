with open("poem.txt", "r") as f:
    print(f.read())

with open("poem.txt", "r") as f:
    if("Twinkle" in f.read()):
        print(" Yes the word 'Twinkle' is present ! ")
    else:
        print("The word 'Twinkle' is not present" )
