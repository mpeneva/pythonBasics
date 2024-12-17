annual_fee = float(input())

basketball_shoes = annual_fee - annual_fee * 0.4
basketball_clothes = basketball_shoes - basketball_shoes * 0.2
basketball_ball = 1/4 * basketball_clothes
basketball_accessories = 1/5 * basketball_ball

total = (annual_fee +
         basketball_clothes +
         basketball_shoes +
         basketball_ball +
         basketball_accessories)

print(f"{total:.2f}")