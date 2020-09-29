import csv

condition = True

while(condition):
    print("Enter the student information :")
    name = input("Name : ")
    age = input("Age : ")
    phone = input("Contact_number : ")
    mail = input("Email_ID : ")
    student_info = str(name +" "+ age +" "+ phone +" "+ mail)
    student_info = student_info.split()
    
    print("\nName : {}\nAge : {}\nContact_number : {}\nEmail_ID : {}\n".format(student_info[0], student_info[1], student_info[2], student_info[3]))
    
    value_check = input("Is the information entered correct?(yes/no)")
    if value_check == "yes":
        with open("Student_Info.csv", "a", newline = '') as csv_file:
            csvwriter = csv.writer(csv_file)
            if csv_file.tell() == 0:
                header = "Name", "Age", "Contact_Number", "Email_ID"
                csvwriter.writerow(header)
            csvwriter.writerow(student_info)
       
        condition_check = input("Do you want to enter the information of another student(yes/no) : ")
        if condition_check == "yes":
            condition = True
        elif condition_check == "no":
            condition = False
    elif value_check == "no":
        print("Re-enter the values!")
