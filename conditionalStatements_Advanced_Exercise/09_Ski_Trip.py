
stay_count = int(input())
room_type = input()
review = input()

total_room_price = float(0)

if room_type == 'room for one person':
    total_room_price = (stay_count-1) * 18.00

elif room_type == 'apartment':
    price_type2 = (stay_count-1) * 25.00

    if stay_count < 10:
        total_room_price = price_type2 - price_type2 * 0.3
    elif 10 <= stay_count <= 15:
        total_room_price = price_type2 - price_type2 * 0.35
    elif stay_count > 15:
        total_room_price = price_type2 - price_type2 * 0.5
elif room_type == 'president apartment':
    price_type3 = (stay_count-1) * 35.00

    if stay_count < 10:
        total_room_price = price_type3 - price_type3 * 0.1
    elif 10 <= stay_count <= 15:
        total_room_price = price_type3 - price_type3 * 0.15
    elif stay_count > 15:
        total_room_price = price_type3 - price_type3 * 0.2

total = float(0)
if review == 'positive':
    total = total_room_price + total_room_price * 0.25
elif review == 'negative':
    total = total_room_price - total_room_price * 0.1


print(f'{total:.2f}')
