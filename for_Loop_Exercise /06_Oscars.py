actor_name = input()
academy_points = float(input())
n = int(input())

award_points = 0

for i in range(1, n+1):
    name = input()
    points = float(input())

    award_points = academy_points + (len(name) * points / 2)
    academy_points = award_points
    if award_points >= 1250.50:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {award_points:.1f}!")
        break
else:
    print(f"Sorry, {actor_name} you need {(1250.50-award_points):.1f} more!")