city = input()
quantity = float(input())

commission = float(0)
if city == "Sofia":
    if 0 <= quantity <= 500:
        commission = quantity * 0.05
    elif 500 < quantity <= 1000:
        commission = quantity * 0.07
    if  1000 < quantity <= 10000:
        commission = quantity * 0.08
    elif quantity > 10000:
        commission = quantity * 0.12
elif city == 'Varna':
    if 0 <= quantity <= 500:
        commission = quantity * 0.045
    elif 500 < quantity <= 1000:
        commission = quantity * 0.075
    if 1000 < quantity <= 10000:
        commission = quantity * 0.1
    elif quantity > 10000:
        commission = quantity * 0.13
elif city == 'Plovdiv':
    if 0 <= quantity <= 500:
        commission = quantity * 0.055
    elif 500 < quantity <= 1000:
        commission = quantity * 0.08
    if 1000 < quantity <= 10000:
        commission = quantity * 0.12
    elif quantity > 10000:
        commission = quantity * 0.145

if city not in ["Sofia", "Plovdiv", "Varna"] or quantity < 0 :
    print("error")
else:
    print(f"{commission:.2f}")