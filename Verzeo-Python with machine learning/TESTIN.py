class Student:
    college_name = "NIT" # class attribute

    def __init__(self,name,age,dob):
        print("Constructor has been called")
        self.name=name
        self.age=age
        self.dob=dob
        
        
    def print_name(self):
        print("Student name: "+self.name)
    def inc(self):
        self.age+=1
        print("Age for student "+self.name+" is: "+str(self.age))


student_1 = Student("Edward",22,"09/05/1977")
student_2 = Student("Connor",21,"14/03/1987")
print(student_1.college_name) 
print(student_2.college_name) 
print(student_1.name,student_1.age,student_1.dob)
print(student_2.name,student_2.age,student_2.dob)

student_1.print_name()
student_1.inc()