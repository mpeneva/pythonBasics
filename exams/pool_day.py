from math import ceil

number_of_persons = int(input())
enter_fee = float(input())
sun_lounger_price = float(input())
sun_umbrela_price = float(input())


########################
total_enter_fee = number_of_persons * enter_fee
total_sun_umbrela_price = sun_umbrela_price * ceil(number_of_persons * 0.5)
total_sun_lounger_price = sun_lounger_price * ceil(number_of_persons * 0.75)

total_expenses = total_enter_fee + total_sun_umbrela_price + total_sun_lounger_price
print(f"{total_expenses:.2f} lv.")