# import datetime
import random

peoplelist=[]
complimentlist=[]

with open('People.txt') as f:
    for line in f:
        l1 = line.strip()
        peoplelist.append(l1)

with open('Compliment.txt') as f:
    for line in f:
        l2 = line.strip()
        complimentlist.append(l2)

num1=(random.randrange(10))
num2=(random.randrange(10))
p=peoplelist[num1]
c=complimentlist[num2]

print(p+" "+c)

# x = datetime.datetime.now()

# print()
# print("The date and time are:")
# print(str(x.day) + "/" + str(x.month) + "/" + str(x.year) + " at " + str(x.hour))

# f.close()
