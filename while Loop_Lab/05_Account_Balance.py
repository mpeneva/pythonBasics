n = input()
total_money = 0.0

while n != 'NoMoreMoney':
    money = float(n)
    if money < 0:
        print("Invalid operation!")
        break

    total_money += money
    print(f"Increase: {money:.2f}")
    n = input()

print(f"Total: {total_money:.2f}")


