# Първи ред – джобните на Тереза на ден – реално число в интервала [1.00 ...100.00]
# Втори ред – парите, които тя печели на ден от продажби – реално число в интервала [1.00...1000.00]
# Трети ред – разходите на Тереза за целия период – реално число в интервала [1.00...1000.00]
# Четвърти ред – цената на подаръка – реално число в интервала [1.00...10000.00]

# Спестени пари от джобни: 5 дни * 5.12 = 25.60
# Спечелени пари: 5 дни * 32.05 = 160.25
# Общо спестени пари: 25.60  + 160.25 = 185.85
# Изваждаме разходите: 185.85 - 15 = 170.85
# Проверяваме дали парите са достатъчни: 170.85 > 150 => парите са достатъчни.

daily_money_per_day = float(input())
daily_profit = float(input())
razhodi_5days = float(input())

present_price = float(input())

#money saved for 5 days
money = daily_money_per_day * 5

#profit for 5 days
profit = daily_profit * 5

money_saved = money + profit
money_total = money_saved - razhodi_5days

if money_total > present_price:
    print(f"Profit: {money_total:.2f} BGN, the gift has been purchased."
)
else:
    print(f"Insufficient money: {present_price-money_total:.2f} BGN.")
