strawberry_price = float(input())

bananas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())

#prices per 1kg
raspberries_price_per_1kg = 1/2 * strawberry_price
oranges_price_per_1kg = raspberries_price_per_1kg - raspberries_price_per_1kg * 0.4
bananas_price_per_1kg = raspberries_price_per_1kg - raspberries_price_per_1kg * 0.8

#total price for Maria
total_strawberries_price = strawberry_price * strawberries_kg
total_raspberries_price = raspberries_price_per_1kg * raspberries_kg
total_oranges_price = oranges_price_per_1kg * oranges_kg
total_bananas_price = bananas_price_per_1kg * bananas_kg

#total
total = total_bananas_price + total_oranges_price + total_raspberries_price + total_strawberries_price
print(f"{total:.2f}")

