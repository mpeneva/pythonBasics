from typing import final

area_for_greening = float(input())

area_price = area_for_greening * 7.61
discount_price = area_price * 0.18
final_price = area_price - discount_price

print(f"The final price is: {final_price} lv." )
print(f"The discount is: {discount_price} lv.")