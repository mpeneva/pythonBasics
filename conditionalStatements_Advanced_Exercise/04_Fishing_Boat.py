budget = int(input())
season = input() #"Spring", "Summer", "Autumn", "Winter"
fishmen_count = int(input())

SPRING_RENT_PRICE = 3000
SUMMER_RENT_PRICE = 4200
AUTUMN_RENT_PRICE = 4200
WINTER_RENT_PRICE = 2600

price = float(0)
if fishmen_count <= 6:
    if season == 'Spring':
        price = SPRING_RENT_PRICE - SPRING_RENT_PRICE * 0.1
    elif season == 'Summer':
        price = SUMMER_RENT_PRICE - SUMMER_RENT_PRICE * 0.1
    elif season == 'Autumn':
        price = AUTUMN_RENT_PRICE - AUTUMN_RENT_PRICE * 0.1
    elif season == 'Winter':
        price = WINTER_RENT_PRICE - WINTER_RENT_PRICE * 0.1
elif 7 < fishmen_count <= 11:
    if season == 'Spring':
        price = SPRING_RENT_PRICE - SPRING_RENT_PRICE * 0.15
    elif season == 'Summer':
        price = SUMMER_RENT_PRICE - SUMMER_RENT_PRICE * 0.15
    elif season == 'Autumn':
        price = AUTUMN_RENT_PRICE - AUTUMN_RENT_PRICE * 0.15
    elif season == 'Winter':
        price = WINTER_RENT_PRICE - WINTER_RENT_PRICE * 0.15
elif fishmen_count > 12:
    if season == 'Spring':
        price = SPRING_RENT_PRICE - SPRING_RENT_PRICE * 0.25
    elif season == 'Summer':
        price = SUMMER_RENT_PRICE - SUMMER_RENT_PRICE * 0.25
    elif season == 'Autumn':
        price = AUTUMN_RENT_PRICE - AUTUMN_RENT_PRICE * 0.25
    elif season == 'Winter':
        price = WINTER_RENT_PRICE - WINTER_RENT_PRICE * 0.25

if (fishmen_count % 2 == 0) and (season != "Autumn"):
    price = price - price * 0.05

if price <= budget:
    print(f"Yes! You have {(budget - price):.2f} leva left.")
else:
    print(f"Not enough money! You need {(price-budget):.2f} leva.")