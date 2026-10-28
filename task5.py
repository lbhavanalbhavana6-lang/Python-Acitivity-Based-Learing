days = int(input("Enter number of days in month: "))
start = int(input("Enter starting weekday (0=Sun, 1=Mon, ..., 6=Sat): "))

print("\n SUN MON TUE WED THU FRI SAT")

day = 1

for week in range(6):

    for weekday in range(7):

        if week == 0 and weekday < start:
            print("    ", end="")

        elif day <= days:
            print("%4d" % day, end="")
            day = day + 1

        else:
            print("    ", end="")

    print()

    if day > days:
        break