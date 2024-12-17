budget = float(input())

video_cards_count = int(input())
processors_count = int(input())
memory_count = int(input())

video_card_price = 250
processor_price = 0.35 * video_cards_count * video_card_price
memory_price = 0.1 * video_cards_count * video_card_price

total_price = video_cards_count * video_card_price + processor_price * processors_count + memory_price * memory_count
if video_cards_count > processors_count:
    total_price = total_price - 0.15 * total_price

if budget >= total_price:
    print(f"You have {(budget - total_price):.2f} leva left!")
else:
    print(f"Not enough money! You need {(total_price - budget):.2f} leva more!")
