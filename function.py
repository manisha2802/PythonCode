#function without parameters
def greet():
    print("Hello world")
greet()

#function with parameters
def add(a,b):
    z=a+b
    print("Addition=",z)

add(10,20)
add(50,50)
add(60,70)

#function with parameters and return types 
def sub(a,b):
    return a-b

z=sub(30,20)
print("Substraction=",z)