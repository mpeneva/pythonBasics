from math import ceil

product = input()
city = input()
quantity = float(input())

total_price = 0

if city == 'Sofia' :
    if product == 'coffee':
        total_price = quantity * 0.5
    elif product == 'water':
        total_price = quantity * 0.80
    elif product == 'beer':
        total_price = quantity * 1.20
    elif product == 'sweets':
        total_price = quantity * 1.45
    elif product == 'peanuts':
        total_price = quantity * 1.60

elif city == 'Plovdiv':
    if product == 'coffee':
        total_price = quantity * 0.40
    elif product == 'water':
        total_price = quantity * 0.70
    elif product == 'beer':
        total_price = quantity * 1.15
    elif product == 'sweets':
        total_price = quantity * 1.30
    elif product == 'peanuts':
        total_price = quantity * 1.50
elif city == 'Varna':
    if product == 'coffee':
        total_price = quantity * 0.45
    elif product == 'water':
        total_price = quantity * 0.70
    elif product == 'beer':
        total_price = quantity * 1.10
    elif product == 'sweets':
        total_price = quantity * 1.35
    elif product == 'peanuts':
        total_price = quantity * 1.55
if city == 'Sofia' or city == 'Plovdiv' or city == 'Varna':
    print(total_price)