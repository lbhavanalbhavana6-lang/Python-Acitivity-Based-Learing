seats = [
    [101, 102, "R", 104],
    [105, 102, "R", None],
    [109, 110, 111, 112]
]

roll_numbers = [101, 102, 104, 105, 106, 109, 110, 111, 112]

print("--- SEATING VALIDATION ---")

students = []

for i in range(len(seats)):
    for j in range(len(seats[i])):

        seat = seats[i][j]

        if seat == "R":
            print("Reserved seat at", i, j)

        elif seat is None:
            print("Empty seat at", i, j)

        elif seat not in roll_numbers:
            print("Invalid student allocation:", seat)

        elif seat in students:
            print("Duplicate roll number:", seat)

        else:
            students.append(seat)
            print("Valid seat:", seat)

print("\nTotal Seats:", len(seats) * len(seats[0]))
print("Allocated Students:", len(students))
print("Empty Seats:", sum(row.count(None) for row in seats))