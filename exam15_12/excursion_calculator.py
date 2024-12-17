persons_number = int(input())
season = input()

total = 0

if persons_number <= 5:
    if season == "spring":
        total = persons_number * 50

    elif season == "summer":
        total = persons_number * 48.50 - persons_number * 48.50 * 0.15

    elif season == "autumn":
        total = persons_number * 60

    elif season == "winter":
        total = persons_number * 86 + persons_number * 86 * 0.08

else:
    if season == "spring":
        total = persons_number * 48

    elif season == "summer":
        total = persons_number * 45 - persons_number * 45 * 0.15

    elif season == "autumn":
        total = persons_number * 49.50

    elif season == "winter":
        total = persons_number * 85 + persons_number * 85 * 0.08

print(f"{total:.2f} leva.")