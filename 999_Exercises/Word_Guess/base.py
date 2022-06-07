import random

# with open('wordle.txt') as f:
#     contents = f.read()
#     print(contents)

# f.close()

thislist=['wordle.txt']
r=(random.randrange(2314))
word=str(thislist[r])

for a in range(0,6):
    guess=input("what is your guess: ")
    if(guess==word):
        print("you got the word!")
        break
    else:
        print("wrong")