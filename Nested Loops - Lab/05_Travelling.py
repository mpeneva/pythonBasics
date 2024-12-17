current_money = 0
break_condition = False

while True:
    destination = input()
    if destination == "End":
        break
    vacation_money_needed = float(input())
    current_money = 0
    while current_money < vacation_money_needed:
        money_saved = input()
        current_money += float(money_saved)

        if current_money >= vacation_money_needed:
            print(f'Going to {destination}!')
            break


