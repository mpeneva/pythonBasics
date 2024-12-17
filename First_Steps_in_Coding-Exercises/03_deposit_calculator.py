deposit = float (input())
deposit_period = int(input())
annual_percetage = float(input()) / 100

amount = deposit + deposit_period * ((deposit * annual_percetage) / 12)
print(amount)
