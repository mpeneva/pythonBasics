import re

won_matches_count = 0
lost_matches_count = 0
drawn_matches_count = 0

first_match_result = input()
second_match_result = input()
third_match_result = input()

first_match_split = re.split(":", first_match_result)
second_match_split = re.split(":", second_match_result)
third_match_split = re.split(":", third_match_result)

#won and lost count
if first_match_split[0] > first_match_split[1] and (first_match_split[0] != first_match_split[1]):
    won_matches_count += 1
elif first_match_split[0] < first_match_split[1] and (first_match_split[0] != first_match_split[1]):
    lost_matches_count += 1

if second_match_split[0] > second_match_split[1] and (second_match_split[0] != second_match_split[1]):
    won_matches_count += 1
elif second_match_split[0] < second_match_split[1] and (second_match_split[0] != second_match_split[1]):
    lost_matches_count += 1

if third_match_split[0] > third_match_split[1] and (third_match_split[0] != third_match_split[1]):
    won_matches_count += 1
elif third_match_split[0] < third_match_split[1] and (third_match_split[0] != third_match_split[1]):
    lost_matches_count += 1

#drawn count
if first_match_split[0] == first_match_split[1] :
    drawn_matches_count += 1

if second_match_split[0] == second_match_split[1]:
    drawn_matches_count  = drawn_matches_count + 1

if third_match_split[0] == third_match_split[1]:
    drawn_matches_count = drawn_matches_count + 1

print(f"Team won {won_matches_count} games.")
print(f"Team lost {lost_matches_count} games.")
print(f"Drawn games: {drawn_matches_count}")
