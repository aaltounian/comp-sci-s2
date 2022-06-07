numbers=[6,9,32,28,15,22,3,18]

mini=numbers[0]
for i in mynumbers:
    if i<mini:
        mini=i
print("minimum: "+str(mini))

maxi=numbers[0]
for i in numbers:
    if i>maxi:
        maxi=i
print("maximum: "+str(maxi))

average=0
a=0
for i in numbers:
    average=average+i
    a=a+1
average=average/a

print("average: "+str(average))
