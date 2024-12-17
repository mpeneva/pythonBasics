budget = float(input())

nights_count = int(input())
night_price = float(input())

extra_expenses = float(input()) / 100

money = 0
if nights_count > 7:
    night_price = night_price - night_price * 0.05

money = nights_count * night_price + extra_expenses * budget

if money <= budget:
    print(f"Ivanovi will be left with {(budget - money):.2f} leva after vacation.")
else:
    print(f"{(money-budget):.2f} leva needed.")