length=int(input("what line length do you want: "))
hv=input("horizontal (h) or vertical (v): ")
if(hv=="h"):
    for x in range(0,length):
        print("*")
if(hv=="v"):
    for x in range(0,length):
        print("*", end="")
