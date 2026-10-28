classrooms = [
    ["Empty", "Reserved", "Empty", "Empty"],
    ["Empty", "Empty", "Reserved", "Empty"],
    ["Empty", "Empty", "Empty", "Empty"]
]

students = ["Ravi", "Priya", "Ravi", "Arun"]

# Allocate students
for student in students:

    found = False

    for room in classrooms:
        for i in range(len(room)):

            if room[i] == "Empty":
                room[i] = student
                found = True
                break

        if found:
            break

    if not found:
        print(student, "No seat available")


# Display classrooms
print("\n--- CLASSROOM DETAILS ---")

for i in range(len(classrooms)):
    print("\nClassroom", i + 1)

    for seat in classrooms[i]:
        print(seat)


# Check duplicate assignments
print("\n--- DUPLICATE STUDENTS ---")

names = []

for room in classrooms:
    for seat in room:

        if seat != "Empty" and seat != "Reserved":

            if seat in names:
                print(seat, "is assigned more than once")

            else:
                names.append(seat)


# Calculate vacant seats
total = 0
vacant = 0

for room in classrooms:
    for seat in room:

        total += 1

        if seat == "Empty":
            vacant += 1

print("\nTotal Seats:", total)
print("Vacant Seats:", vacant)
print("Occupied Seats:", total - vacant)