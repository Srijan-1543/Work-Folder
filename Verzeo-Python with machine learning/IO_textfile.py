obj=open("tempo.txt")
print(obj)
content=obj.readlines()
print(content)
print(type(content))
obj.close()

obj=open("tempo.txt")
content=obj.read()
print(content)
print(type(content))
obj.seek(0)
content=obj.readline()
print(content)
print(type(content))
content=obj.readline()
print(content)
print(type(content))
content=obj.readline()
print(content)
print(type(content))
content=obj.readline()
print(content)
print(type(content))
obj.close()

obj=open('msg.txt','w')
ls=["HALLO\n","NEWLINE\t","TAB USED\n","dog"]
obj.write("FIRSTTT\n")
obj.writelines(ls)
obj.close()



