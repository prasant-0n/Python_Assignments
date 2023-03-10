# Write a python program to store details of a student like rollno, regdno, name, branch, stream, sem, phone no, address in dictionary and print the details in cv format student_details = {}

student_details = {}

# get input from user and store in dictionary
student_details["Roll No"] = input("Enter Roll No: ")
student_details["Regd No"] = input("Enter Regd No: ")
student_details["Name"] = input("Enter Name: ")
student_details["Branch"] = input("Enter Branch: ")
student_details["Stream"] = input("Enter Stream: ")
student_details["Sem"] = input("Enter Sem: ")
student_details["Phone No"] = input("Enter Phone No: ")
student_details["Address"] = input("Enter Address: ")

# print details in CV format
print("\nCV Format")
print("----------")
print(f"Roll No: {student_details['Roll No']}")
print(f"Regd No: {student_details['Regd No']}")
print(f"Name: {student_details['Name']}")
print(f"Branch: {student_details['Branch']}")
print(f"Stream: {student_details['Stream']}")
print(f"Sem: {student_details['Sem']}")
print(f"Phone No: {student_details['Phone No']}")
print(f"Address: {student_details['Address']}")
