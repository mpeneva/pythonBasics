pens_count = int(input())
markers_count = int(input())
cleaning_liquid = int(input())
discount_percentage = float(input()) / 100

pens = 5.80 * pens_count
markers = 7.20 * markers_count
cleaning = 1.20 * cleaning_liquid

amount = pens + markers + cleaning
amount_discount = amount - (amount * discount_percentage)

print(amount_discount)
