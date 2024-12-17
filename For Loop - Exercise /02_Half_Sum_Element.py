import sys

n = int(input())

max_number = -sys.maxsize
sum_numbers = 0

for i in range(0,n):
    num = int(input())
    if num > max_number:
        max_number = num
    sum_numbers += num


if max_number == sum_numbers - max_number:
    print("Yes")
    print("Sum =",max_number)
else:
    sum_numbers = sum_numbers - max_number
    print("No")
    print("Diff =", abs(max_number - sum_numbers))

