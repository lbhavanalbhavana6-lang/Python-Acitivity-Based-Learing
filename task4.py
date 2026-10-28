# Student Email and Identifier Validation

email = input("Enter student email: ")
reg_id = input("Enter registration ID: ")

# Email validation
if "@" in email and "." in email and " " not in email:
    print("Email is Valid")
else:
    print("Email is Invalid")

# Registration ID validation
if reg_id.startswith("STU") and reg_id[3:].isdigit() and len(reg_id) == 8:
    print("Registration ID is Valid")
else:
    print("Registration ID is Invalid")