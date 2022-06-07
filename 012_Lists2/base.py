import random

a=int(input("how many random numbers do u want: "))
thislist=[1,2,3,4,5,6,7,8,9,10]
for i in range(0,a-1):
    r=(random.randrange(9))
    print(str(thislist[r]), end=", ")
r2=(random.randrange(9))
print(str(thislist[r2]))
