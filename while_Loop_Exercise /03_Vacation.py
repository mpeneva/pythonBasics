#нужни пари
needed_money = float(input())
#наличн пари
owned_money = float(input())

days_counter = 0
spending_counter = 0

while owned_money < needed_money and spending_counter < 5:
    #action
    command = input()
    money = float(input())
    days_counter += 1

    if command == 'save':
        spending_counter = 0
        owned_money += money

    elif command == 'spend':
        owned_money -= money
        spending_counter += 1

        if owned_money < 0:
            owned_money = 0
else:
    if spending_counter == 5:
        print(f"You can\'t save the money.")
        print(f"{days_counter}")
    if owned_money >= needed_money:
        print(f"You saved the money for {days_counter} days.")