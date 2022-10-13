import os
name = input("Enter Complete Filename: ")
x = os.path.splitext(name)
print("The File Extension is: ", x[1])

if x[1] == ".py":
   print("python file")
else:
   print("not python file")
