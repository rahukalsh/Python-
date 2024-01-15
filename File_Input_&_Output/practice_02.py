
import random


def game():
    myscore = random.randint(1,300)
    print(f"The Score is {myscore}")
    return(myscore)

score = game()
with open("hiscore.txt", "r") as f:
    highscore = int(f.read())
if(score > highscore):
    with open("hiscore.txt", "w") as f:
        f.write(str(score))
         