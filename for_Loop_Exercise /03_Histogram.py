n = int(input())

number_count_less200 = 0
number_count_200_399 = 0
number_count_400_599 = 0
number_count_600_799 = 0
number_count_more800 = 0

for i in range (0,n):
    number = int(input())
    if number < 200:
        number_count_less200 += 1
    elif 200 <= number <= 399:
        number_count_200_399 += 1
    elif 400 <= number <= 599:
        number_count_400_599 += 1
    elif 600 <= number <= 799:
        number_count_600_799 += 1
    elif number >= 800:
        number_count_more800 += 1
#< 200
p1 = (number_count_less200 / n) * 100
#[200, 399]
p2 = (number_count_200_399 / n) * 100
#[400, 599]
p3 = (number_count_400_599 / n) * 100
#[600, 799]
p4 = (number_count_600_799 / n) * 100
#>=800
p5 = (number_count_more800 / n) * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")