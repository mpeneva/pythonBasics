# Цената на един литър гориво е 2.10 лв.
# Цената за екскурзовод е 100лв.
# В зависимост от деня има отстъпки от общата цена - за събота 10%, а за неделя 20%

fuel_liter = 2.10
guide = 100
saturday_discount = 0.1
sunday_discount = 0.2

budget = float(input())
fuel_needed_liter = float(input())
vacation_day = input() #"Saturday" or "Sunday"

############################################################
money_needed = fuel_needed_liter * fuel_liter + guide

if vacation_day == 'Sunday':
    money_needed = money_needed - money_needed * 0.2
else:
    money_needed = money_needed - money_needed * 0.1

if money_needed <= budget:
    print(f"Safari time! Money left: {(budget-money_needed):.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {(money_needed - budget):.2f} lv.")

