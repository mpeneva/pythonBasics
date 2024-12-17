flower = input()
flower_count = int(input())
budget = float(input())

total = 0

if flower == "Roses":
    if flower_count > 80:
        price = flower_count * 5
        total = price - price * 0.1
    else:
        total = flower_count * 5
elif flower == "Dahlias":
    if flower_count > 90:
        price = flower_count * 3.80
        total = price - price * 0.15
    else:
        total = flower_count * 3.80
elif flower == "Tulips":
    if flower_count > 80:
        price = flower_count * 2.80
        total = price - price * 0.15
    else:
        total = flower_count * 2.80
elif flower == "Narcissus":
    if flower_count < 120:
        price = flower_count * 3
        total = price + price * 0.15
    else:
        total = flower_count * 3
elif flower == "Gladiolus":
    if flower_count < 80:
        price = flower_count * 2.50
        total = price + price * 0.2
    else:
        total = flower_count * 2.50
if total <= budget:
    print(f"Hey, you have a great garden with {flower_count} {flower} and {(budget - total):.2f} leva left.")
else:
    print(f"Not enough money, you need {(total - budget):.2f} leva more.")