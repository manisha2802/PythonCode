a=[10,20,45,15,60,80]
k=95
for i in a:
    for j in a:
        if i+j==k:
            print(i,j)
        else:
            print("Bad")