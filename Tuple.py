a=(10,20,78,10,86,30,94)
print(type(a))

for i in a:
    print(i)

for i in range(len(a)):
    print(i)
    if(i==3):
        break
    print(a[i])

for i in range(len(a)):
    print(i)
    if(i==3):
        continue
    print(a[i])

# Slicing

print(a[1:3])
print(a[-6:4])
print(a[::-1])

b=()
print(type(b))

c=10,
print(c)

#Tuple Methods
print(min(a))
print(max(a))
print(a.count(10))
print(a.index(20))

s= sorted(a)
print(a)
print(s)

# in and not in operators

if(10 in a):
    print('present in the A')
else:
    print("Not present")

a1=(5,2,6,3)
a2=0
for i in a1:
    if(type(i)==int):
        a2=a2+i
print(a2)


