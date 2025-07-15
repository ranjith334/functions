fact=1
def factorial(n):
    global fact
    fact=1
    for i in range (1,n+1):
        fact*=i
        
    

num=int(input("Enter a number"))
if num<0:
    print("cannot derive a fact for -ve numbers")
else:
    factorial(num)    
    print(f"factoprial of {num} is",fact)
    