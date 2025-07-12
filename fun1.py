'''def mul_by(n):
    def inner(x):
        return x*n
    return inner    
times_2=mul_by(2)    
times_3=mul_by(3)
print(times_2(5))
print(times_3(10))'''

def great(text):
    def inner(name):
        return f "{text},{name}"
    return inner  
hi=great("hello")
print("vijay")
