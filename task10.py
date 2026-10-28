# Internship Candidate Ranking

candidates = []

n = int(input("Enter number of candidates: "))

for i in range(n):

    print("\nEnter Candidate Details")

    name = input("Enter candidate name: ")
    marks = float(input("Enter academic marks: "))
    assessment = float(input("Enter assessment score: "))
    attendance = float(input("Enter attendance: "))

    # Eligibility conditions
    if marks >= 60 and assessment >= 50 and attendance >= 75:

        total = marks + assessment

        candidates.append([name, marks, assessment, attendance, total])

        print("Eligible")

    else:
        print("Not Eligible")


# Ranking candidates
candidates.sort(key=lambda x: (-x[4], -x[1], -x[3]))

print("\n--- INTERNSHIP RANKING ---")

for i, c in enumerate(candidates):

    print("\nRank:", i + 1)
    print("Name:", c[0])
    print("Marks:", c[1])
    print("Assessment:", c[2])
    print("Attendance:", c[3])
    print("Total Score:", c[4])