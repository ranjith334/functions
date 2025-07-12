x=100
y=10
def display():
    x=22
    print("x= ",x)
    print("locally", x)
display()    
print("x= ",x)
y=10
y=25
print("latest value of y globally: ",y)
print("globally", x+y)


