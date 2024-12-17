n = int(input())

odd_sum = 0
even_sum = 0

for number in range(n):
    entry = int(input())
    if number % 2 == 0 :
        even_sum += entry
    else:
        odd_sum += entry

if odd_sum == even_sum:
    print("Yes\nSum =",odd_sum)
else:
    print("No\nDiff =", abs(odd_sum - even_sum))