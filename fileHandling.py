fileRead=open(r"D:\first.txt","w")
fileRead.write("Hello\n Welcome")
fileRead.close()


f=open(r"D:\first.txt","r")
print(f.read())

# f=open(r'D:\Python_9AM\second.txt','x')
# f.write("Hello, How are you?")
# f.close()

f=open(r'D:\Python_9AM\second.txt','r')
print(f.read())
print(f.mode)
f.close()

f=open(r'D:\Python_9AM\second.txt','a')
f.write("\nI am fine ,Thank you")
f.close()

f=open(r'D:\Python_9AM\second.txt','r')
print(f.read(5))
print(f.readline())
print(f.readline())
print(f.mode)

f.seek(0)
for i in f:
    print(i)
f.close()

#readlines
f1=open(r'D:\Python_9AM\second.txt','r')
#print(f1.readlines())
print(f1.readlines()[0])
 
print("**# content manager readlines*****")

with open(r"D:\Python_9AM\fourth.txt", "x") as f6:
    f6.write("Hello, I am learning python")
    print(f6.mode)
    f6.close()

    
