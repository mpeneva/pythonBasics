from sys import set_coroutine_origin_tracking_depth

budget = float(input())
season = input() #summer, winter

destination = ""
vacation_place = ""
expenses = float(0)

if budget <= 100 :
    if season == "summer":
        vacation_place = "Camp"
        destination = "Bulgaria"
        expenses = budget * 0.3
    elif season == "winter":
        vacation_place = "Hotel"
        destination = "Bulgaria"
        expenses = budget * 0.7
elif 100 < budget <= 1000:
    if season == "summer":
        destination = "Balkans"
        vacation_place = "Camp"
        expenses = budget * 0.4
    elif season == "winter":
        destination = "Balkans"
        vacation_place = "Hotel"
        expenses = budget * 0.8
elif budget > 1000:
    destination = "Europe"
    vacation_place = "Hotel"
    expenses = budget * 0.9

if destination == "Bulgaria":
    print(f"Somewhere in {destination}")
elif destination == "Balkans":
    print(f"Somewhere in {destination}")
elif destination == "Europe":
    print(f"Somewhere in {destination}")

print(f"{vacation_place} - {expenses:.2f}")
