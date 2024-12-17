from math import floor
from math import ceil

tennis_racket_price = float(input())

tennis_racket_count = int(input())
tennis_shoes_count = int(input())

tennis_shoes_price = tennis_racket_price / 6
tennis_rackets_And_shoes_price = (tennis_racket_price * tennis_racket_count +
                                  tennis_shoes_price *tennis_shoes_count)

total_tennis_equipment_price = 0.2 * tennis_rackets_And_shoes_price
total_price = (tennis_racket_price * tennis_racket_count +
               tennis_shoes_price * tennis_shoes_count +
               total_tennis_equipment_price)

print(f"Price to be paid by Djokovic {floor(1/8 * total_price)}")
print(f"Price to be paid by sponsors {ceil(7/8 * total_price)}")