days = int(input())

rakia_all = 0
gradus_all = 0

for i in range(1, days+1):
    rakia_liter = float(input())
    rakia_all += rakia_liter

    gradus_rakia = float(input()) * rakia_liter
    gradus_all += gradus_rakia

print(f"Liter: {rakia_all:.2f}")
print(f"Degrees: {gradus_all/rakia_all:.2f}")
if (gradus_all/rakia_all) < 38:
    print(f"Not good, you should baking!")
elif 38 <= (gradus_all/rakia_all) <= 42:
    print("Super!")
else:
    print("Dilution with distilled water!")