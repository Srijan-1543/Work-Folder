import csv
def write_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Contact Number","E-Mail ID"])   
        writer.writerow(info_list)

if __name__=="__main__":
    condition = True
    student_num=1
    while(condition):
        student_info=input("Enter student information for student #{} in the following format (Name Age Contact Email): ".format(student_num))
        student_list = student_info.split(' ')
        print("Entered spilt up information: "+str(student_list))
        print("\nThe Entered Information is :\nName: {}\nAge: {}\nContact_number: {}\nE-Mail ID: {}".format(student_list[0],student_list[1],student_list[2],student_list[3]))
        choice=input("Is the entered information correct? (yes/no)").lower()
        if choice =="yes":
            write_csv(student_list)
            condition_check=input("Enter (yes/no) if u want to continue: ").lower()
            if condition_check=="yes":
                condition = True
                student_num+=1
            elif condition_check=="no":
                condition = False
        elif choice =="no":
            print("Please Re-Enter the information!")

