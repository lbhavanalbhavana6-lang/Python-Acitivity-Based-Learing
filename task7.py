teams = []

n = int(input("Enter number of teams: "))

for i in range(n):

    print("\nEnter Team Details")

    name = input("Enter team name: ")
    members = int(input("Enter number of members: "))

    if members < 2 or members > 4:
        print("Invalid Team Size")
        continue

    round1 = int(input("Enter Round 1 score: "))
    round2 = int(input("Enter Round 2 score: "))
    round3 = int(input("Enter Round 3 score: "))

    total = round1 + round2 + round3

    teams.append([name, total, round3])

# Ranking teams
teams.sort(key=lambda x: (-x[1], -x[2]))

print("\n--- HACKATHON RANKING ---")

for i, team in enumerate(teams):

    print("\nRank:", i + 1)
    print("Team:", team[0])
    print("Total Score:", team[1])
    print("Final Round Score:", team[2])