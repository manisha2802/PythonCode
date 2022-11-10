dict={
    "name":"Manisha",
    "city":"Pune"
}
print(dict)
print(dict['city'])

dict['age']=28
print(dict)

dict.update(name="Rani")
print(dict)

dict1=dict.copy()
print(dict1)
del dict['age']
print(dict)
print(dict1)

dict['Skills']=["Python",'Js',"Java"]
print(dict)
print(dict1)

