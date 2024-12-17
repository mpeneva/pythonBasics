from math import floor

contests_count = int(input())
actual_points = int(input())

W_points = 2000
F_points = 1200
SF_points = 720

points = 0
gain_points = 0
gain_match_count = 0

for i in range(contests_count):
    contest = input()
    if contest == 'W':
        points = actual_points + W_points
        actual_points = points
        gain_points += W_points
        gain_match_count += 1

    elif contest == 'F':
        points = actual_points + F_points
        actual_points = points
        gain_points += F_points

    elif contest == 'SF':
        points = actual_points + SF_points
        actual_points = points
        gain_points += SF_points

print(f"Final points: {points}")
print(f"Average points: {floor(gain_points/contests_count)}")
print(f"{(gain_match_count/contests_count)*100:.2f}%")
