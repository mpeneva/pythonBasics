number = int(input())
bonus = 0

#getting bonus

if number <= 100 :
    bonus = 5
elif 100 < number <= 1000 :
    bonus = 0.2 * number
else:
    bonus = 0.1 * number

#additional bonus
if number % 2 == 0 :
    bonus += 1
elif number % 10 == 5:
    bonus = bonus + 2

print(bonus)
print(bonus + number)

