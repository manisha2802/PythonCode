# in and not in  

li=["Manisha","Rani","Kajal"]
print("Rani" in li)

print("Kajal" not in li)

if("Rani" in li):
    print("Present in list")
else:
    print("Not present")

# Program 2

name=input("Enter the Name:")
if name in li:
    print("Name is present in list")
else:
    print('Name is not present in list')

# Program 3 
m1=int(input("Enter the marks of Marathi: "))
m2=int(input("Enter the marks of Hindi: "))
m3=int(input("Enter the marks of English: "))

avg1=((m1+m2+m3)/3)
print(avg1)

print("The marks for Marathi {}".format(m1))
print("The marks for Hindi {}".format(m2))
print("The marks for English {}".format(m3))