items=int(input("how many items are you purchasing: "))
total=0;

for a in range(0,items):
    name=input("whats the name of the item: ")
    amount=float(input("how much does the item cost: "))
    total=total+amount
    
print("the total is: "+str(total))