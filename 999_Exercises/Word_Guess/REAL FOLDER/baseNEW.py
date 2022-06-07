import random

thislist=[]
with open('allow_words.txt') as f:
    for line in f:
        l = line.strip()
        thislist.append(l)

f.close()

num=(random.randrange(12972))
word=thislist[num]

for a in range(0,6):
    guess=input("what is your guess: ")
    if guess==word:
        print("correct")
        a=1
        break
    else:
        print("wrong")
if a==0:
    print("you lost the game, the word was: "+word)