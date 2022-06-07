num1=int(input("whats the first number: "))
operation=input("what's the operation: ")
num2=int(input("whats the second number: "))
if(operation=="/"):
    product=num1/num2
    print(str(num1)+operation+str(num2)+" = "+str(product))
if(operation=="*"):
    product=num1*num2
    print(str(num1)+operation+str(num2)+" = "+str(product))
if(operation=="+"):
    product=num1+num2
    print(str(num1)+operation+str(num2)+" = "+str(product))
if(operation=="-"):
    product=num1-num2
    print(str(num1)+operation+str(num2)+" = "+str(product))