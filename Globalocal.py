a=10
def display():
 a=15
 print(a)
display()
print(a)

# Global variable

x=20
def display1():
    global x
    x=30
    print(x)
display1()
print(x)

#Lambda

func=lambda a:a*a
print(func(10))

func2=lambda x,y:x+y
a1=func2(5,6)
print(a1)

func3=lambda a,b:a if a>b else b
print(func3(10,20))

