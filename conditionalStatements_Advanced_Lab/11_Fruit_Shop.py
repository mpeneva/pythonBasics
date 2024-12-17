fruit = input()
day = input()
quantity = float(input())

total_price = 0

if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
    if fruit == 'banana':
        total_price = quantity * 2.50
    elif fruit == 'apple':
        total_price = quantity * 1.20
    elif fruit == 'orange':
        total_price = quantity * 0.85
    elif fruit == 'grapefruit':
        total_price = quantity * 1.45
    elif fruit == 'kiwi':
        total_price = quantity * 2.70
    elif fruit == 'pineapple':
        total_price = quantity * 5.50
    elif fruit == 'grapes':
        total_price = quantity * 3.85
    if fruit not in ["banana", "apple", "orange", "grapefruit", "kiwi", "pineapple","grapes"]:
        print("error")
    else:
        print(f"{total_price:.2f}")
elif day in ['Saturday', 'Sunday']:
    if fruit == 'banana':
        total_price = quantity * 2.70
    elif fruit == 'apple':
        total_price = quantity * 1.25
    elif fruit == 'orange':
        total_price = quantity * 0.90
    elif fruit == 'grapefruit':
        total_price = quantity * 1.60
    elif fruit == 'kiwi':
        total_price = quantity * 3.00
    elif fruit == 'pineapple':
        total_price = quantity * 5.60
    elif fruit == 'grapes':
        total_price = quantity * 4.20
    if fruit not in ["banana", "apple", "orange", "grapefruit", "kiwi", "pineapple","grapes"]:
        print("error")
    else:
        print(f"{total_price:.2f}")
else:
    print("error")