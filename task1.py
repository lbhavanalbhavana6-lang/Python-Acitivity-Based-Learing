students = []

n = int(input("Enter number of students: "))

for i in range(n):

    print("\nEnter Student Details")

    name = input("Enter name: ")
    marks = float(input("Enter aggregate marks: "))

    s1 = float(input("Enter subject 1 marks: "))
    s2 = float(input("Enter subject 2 marks: "))

    attendance = float(input("Enter attendance: "))
    income = float(input("Enter family income: "))

    if (marks >= 75 and s1 >= 40 and s2 >= 40
        and attendance >= 75 and income <= 250000):

        students.append([name, marks, attendance, income])
        print("Eligible")

    else:
        print("Not Eligible")


# Ranking students
students.sort(key=lambda x: (-x[1], -x[2], x[3]))

print("\n--- SCHOLARSHIP RANK LIST ---")

for i, student in enumerate(students):

    print("\nRank:", i + 1)
    print("Name:", student[0])
    print("Marks:", student[1])
    print("Attendance:", student[2])
    print("Income:", student[3])
