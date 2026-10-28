chemicals = []

n = int(input("Enter number of chemicals: "))

for i in range(n):

    print("\nEnter Chemical Details")

    name = input("Enter chemical name: ")
    category = input("Enter storage category: ")
    quantity = float(input("Enter quantity (litres): "))

    max_quantity = float(input("Enter maximum allowed quantity: "))

    if quantity > max_quantity:
        print("Invalid: Maximum quantity exceeded")

    else:
        print("Valid quantity")

    chemicals.append([name, category, quantity])

# Check compatibility
print("\n--- INVENTORY REPORT ---")

for c in chemicals:
    print("\nChemical:", c[0])
    print("Category:", c[1])
    print("Quantity:", c[2])

# Example compatibility restriction
for i in range(len(chemicals)):
    for j in range(i + 1, len(chemicals)):

        if (chemicals[i][1] == "Acid" and
            chemicals[j][1] == "Base") or \
           (chemicals[i][1] == "Base" and
            chemicals[j][1] == "Acid"):

            print("Invalid combination:",
                  chemicals[i][0], "and", chemicals[j][0])