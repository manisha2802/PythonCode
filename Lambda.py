from functools import reduce

#1. Find out the age 
listA=[1990,1992,1993,1998]
listB=[]
for i in listA:
    listB.append(2022-i)
print(listB)

#Using map()
result=list(map(lambda x:2022-x,listA))
print(result)

#2
listC=[10,20,30,40,55,65,45]
listD=[]
for item in listC:
    listD.append(item+10)

print(listD)

print(list(map(lambda x:x+10,listC)))

# filter out the age >30
#3
listE=[25,32,31,45,52,26]
listF=[]
for i in listE:
    if i>30:
        listF.append(i)

print(listF)

#filter()
print(list(filter(lambda x:x>30,listE)))

#4. Find out even numbers
listG=[]
for item in listE:
    if item%2==0:
        listG.append(item)

print(listG)
print(list(filter(lambda x:x%2==0,listE)))

#5.Reduce()

listH=[10,20,30]
print(reduce(lambda x,y:x+y,listH))

