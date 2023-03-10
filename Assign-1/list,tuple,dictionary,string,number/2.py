# . Write a python program to find total and average mark of a student and take 5 different subject along with marks of 10 students using dictionary

marks = {"Maths": [], "Physics": [], "Chemistry": [],
         "English": [], "Computer Science": []}

# Take input for marks of 10 students
for i in range(10):
    print(f"Enter marks for student {i+1}:")
    for subject in marks:
        mark = int(input(f"{subject}: "))
        marks[subject].append(mark)

# Calculate total and average marks for each student
for i in range(10):
    total_marks = sum(marks[subject][i] for subject in marks)
    average_marks = total_marks / len(marks)
    print(
        f"Student {i+1} - Total Marks: {total_marks}, Average Marks: {average_marks}")
