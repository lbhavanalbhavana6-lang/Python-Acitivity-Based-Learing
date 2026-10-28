players = []

n = int(input("Enter number of players: "))

for i in range(n):

    name = input("\nEnter player name: ")

    scores = []

    for j in range(3):
        score = int(input("Enter match score: "))
        scores.append(score)

    total = sum(scores)
    average = total / 3
    highest = max(scores)
    lowest = min(scores)

    players.append([name, scores, total, average, highest, lowest])


# Ranking players
players.sort(key=lambda x: (-x[3], -x[4]))

print("\n--- SPORTS PERFORMANCE REPORT ---")

for i, p in enumerate(players):

    print("\nRank:", i + 1)
    print("Player:", p[0])
    print("Scores:", p[1])
    print("Total Score:", p[2])
    print("Average Score:", round(p[3], 2))
    print("Highest Score:", p[4])
    print("Lowest Score:", p[5])

    if p[1][0] < p[1][1] < p[1][2]:
        print("Trend: Improving")

    elif p[1][0] > p[1][1] > p[1][2]:
        print("Trend: Decreasing")

    else:
        print("Trend: Mixed")

    print("Consistency Range:", p[4] - p[5])