n = int(input())

left_sum = 0
right_sum = 0

for number in range(1, (2 * n) + 1):
    entry = int(input())
    if number <= n :
        left_sum += entry
    else:
        right_sum += entry

if left_sum == right_sum:
    print("Yes, sum =" , left_sum)
else:
    print("No, diff =" , abs(left_sum - right_sum))