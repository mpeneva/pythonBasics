#godini na Lili
n = int(input())
washing_machine_price = float(input())
toy_price = int(input())

even_bd_money = 0
toys_bd_count = 0
bd_money = 10
for i in range(1,n+1):
    if i % 2 == 0:
        even_bd_money += bd_money * (i/2)
    else:
        toys_bd_count += 1

left_money = even_bd_money - 1 * (n // 2)
toys_sell_price = toy_price * toys_bd_count

total = toys_sell_price + left_money

if total >= washing_machine_price:
    print(f"Yes! {(total - washing_machine_price):.2f}")
else:
    print(f"No! {abs(washing_machine_price - total):.2f}")