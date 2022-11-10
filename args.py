def sum1(*args):
    sum1=0
    for i in args:
        sum1+=i
    return sum1

a=sum1(10,30,52,85,75,48,95)
print("Total sum=",a)

def fun1(*a):
    print(a)
    print(type(a))
fun1(10,20,30,40,50)

def fun2(**kwargs):
    print(type(kwargs))
    for i,j in kwargs.items():
     print(i,j)
fun2(first_Name="Manisha",last_Name="Kamble",city="Pune",Job_role="Engineer")

def func3(a,b,c=50):
    print(a+b+c)
func3(b=10,a=20)

print(len.__doc__)
print(print.__doc__)

#default Arguments***

def greet(name,city,greet="Welcome",):
    print(greet,"to",city,name)
greet('Manisha',"Pune")


