students_marks={"Alice":85, "Bob":78, "Charlie":68, "Riva":89}

name=input("Enter the student's name: ")
 
if name in students_marks:
    # print(name,"'s marks: ",students_marks[name]) 
     print(f"{name}'s marks: {students_marks[name]}")
else:
    print("Student not found.")    