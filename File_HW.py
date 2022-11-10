# 1. CREATE TEXT FILE WITH BELOW DATA IN IT AND NAME  IT AS colors.txt
# Brown
# Yellow
# Green

f=open(r'D:\Python_9AM\Color.txt',"w")
f.write("Brown\nYellow\nGreen")
f.close()

#2.READ THE FILE  colors.txt AND DISPLAY THE OUTPUT ON THE SCREEN
f=open(r'D:\Python_9AM\Color.txt',"r")
print(f.read())
f.close()

# 3.ADD BELOW DATA IN THE FILE colors.txt WITHOUT REMOVING OLD DATA
# BLUE
f=open(r'D:\Python_9AM\Color.txt',"a")
f.write("\nBlue")
f.close()

#4.DISLAY THE DATA OF THE FILE colors.txt USING FOR LOOP 
f=open(r'D:\Python_9AM\Color.txt',"r")
for i in f:
    print(i)
f.close()



