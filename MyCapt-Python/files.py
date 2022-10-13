import csv

def write_into_csv(info):
    with open('student_info_csv','a+', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(info)

with open('student_info_csv','w+', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Name","Age","Contact","Email"])


condn =True
print("Enter student information : (Name,Age,Contact,Email)")
while(condn):
    info = input("Info: ")
    stdinfo = info.split(' ')
    print("Student details in split up format: "+str(stdinfo))
    write_into_csv(stdinfo)

    condinfo = input("Enter yes/no:")
    if condinfo =="yes":
        condn = True
    elif condinfo =="no":
        condn = False
