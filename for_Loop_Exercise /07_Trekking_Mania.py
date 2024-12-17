n = int(input())

musala_group = 0
montblan_group = 0
kilimandzaro_group = 0
k2_group = 0
everest_group = 0

for i in range(n) :
    number_person = int(input())

    if number_person <= 5:
        musala_group += number_person
    elif 6 <= number_person <= 12:
        montblan_group += number_person
    elif 13 <= number_person <= 25:
        kilimandzaro_group += number_person
    elif 26 <= number_person <= 40:
        k2_group += number_person
    elif number_person >= 41:
         everest_group += number_person

persons_total = (musala_group +
                 montblan_group +
                 kilimandzaro_group +
                 k2_group +
                 everest_group)

musala_group_p = (musala_group / persons_total) * 100
montblan_group_p = (montblan_group / persons_total) * 100
kilimandzaro_group_p = (kilimandzaro_group / persons_total) * 100
k2_group_p = (k2_group / persons_total) * 100
everest_group_p = (everest_group / persons_total) * 100

print(f"{musala_group_p:.2f}%")
print(f"{montblan_group_p:.2f}%")
print(f"{kilimandzaro_group_p:.2f}%")
print(f"{k2_group_p:.2f}%")
print(f"{everest_group_p:.2f}%")
