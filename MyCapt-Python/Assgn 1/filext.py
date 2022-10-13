import os
name = input("Enter Complete Filename: ")
x = os.path.splitext(name)
print("The File Extension is: ", x[1])
