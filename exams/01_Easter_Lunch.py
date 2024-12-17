# Козунак – 3.20 лв.
# • Яйца – 4.35 лв. за кора с 12 яйца
# • Курабии – 5.40 лв. за килограм
# • Боя за яйца - 0.15 лв. за яйце

easter_cake = 3.20
eggs_package_12 = 4.35
cookies_per1kg = 5.40
egg_color = 0.15

easter_cake_count = int(input())
egg_package_count = int(input())
cookies_kg_count = int(input())

#easter cake
cake_price = easter_cake_count * easter_cake

#eggs packages
eggs_price = egg_package_count * eggs_package_12
egg_price_color = egg_package_count * 12 * 0.15

#cookies
cookies_price = cookies_kg_count * cookies_per1kg

total = cake_price + eggs_price + egg_price_color + cookies_price

print(f'{total:.2f}')

