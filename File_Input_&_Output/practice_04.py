with open("donkey.txt", "r") as f:
    repli = f.read()

repli = repli.replace('donkey', '########')
with open("donkey.txt", "w") as f:
    f.write(repli)


# Now do more thing like replacing the latter 'a' with '@' 