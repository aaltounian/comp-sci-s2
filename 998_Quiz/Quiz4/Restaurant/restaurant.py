import random;

restaurants=["blaze", "in n out", "mcdonalds"]
print(restaurants)
rselect=input("what restaurant would you like to go to: ")
if(rselect=="blaze"):
    blazeoptions=["cheese pizza", "pepperoni pizza", "garlic bread"]
    print("")
    print("our options are: ")
    print(blazeoptions)
    print("")
    r1=(random.randrange(3))
    print("suggested item: "+str(blazeoptions[r1]))
    
if(rselect=="in n out"):
    innoutoptions=["hamburger", "cheeseburger", "shake"]
    print("")
    print("our options are: ")
    print(innoutoptions)
    print("")
    r2=(random.randrange(3))
    print("suggested item: "+str(innoutoptions[r2]))
    
if(rselect=="mcdonalds"):
    mcdonaldsoptions=["pancakes", "salad", "fries"]
    print("")
    print("our options are: ")
    print(mcdonaldsoptions)
    print("")
    r3=(random.randrange(3))
    print("suggested item: "+str(mcdonaldsoptions[r3]))