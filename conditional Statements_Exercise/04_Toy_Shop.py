puzzle = 2.60
doll = 3.00
bear = 4.10
truck = 2.00
minion = 8.20

money_for_vacation_needed = float(input())

puzzle_count = int(input())
doll_count = int(input())
bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

money_left = 0
total_price = puzzle_count * puzzle + doll_count * doll + bear_count * bear + minion_count * minion + truck_count * truck
toys_count = puzzle_count + doll_count + bear_count + minion_count + truck_count

if toys_count >= 50:
    total_price = total_price - total_price* 0.25

money_left = total_price - total_price * 0.1

if money_left >= money_for_vacation_needed:
    print(f"Yes!{abs(money_for_vacation_needed - money_left): .2f} lv left.")
else:
    missing_money = money_for_vacation_needed - money_left
    print(f"Not enough money!{missing_money: .2f} lv needed.")

