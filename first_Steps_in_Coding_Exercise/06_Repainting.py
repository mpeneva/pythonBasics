plastic = int(input()) # in sq.m
paint = int(input()) # in liters
thinner = int(input()) # in liters
working_hours_total = int(input())

plastic_total = (plastic + 2) * 1.50
plastic_extra = 0.40
paint_total = (paint + paint * 0.1) * 14.5
thinner_total = thinner * 5.00

total = plastic_total + plastic_extra + paint_total + thinner_total
working_hour = (total * 30 / 100) * working_hours_total

print(total + working_hour)
