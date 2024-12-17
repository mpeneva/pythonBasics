n1 = int(input())
n2 = int(input())
magic_number = int(input())

combination = 0
break_condition = False

for i in range(n1, n2+1):
    for j in range(n1, n2+1):
        combination += 1
        if i+j == magic_number:
            print(f"Combination N:{combination} ({i} + {j} = {magic_number})")
            break_condition = True
            break
    if break_condition:
        break

else:
    print(f"{combination} combinations - neither equals {magic_number}")