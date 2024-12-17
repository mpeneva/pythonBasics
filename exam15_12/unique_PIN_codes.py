digit1_interval = int(input())
digit2_interval = int(input())
digit3_interval = int(input())

for d1 in range(1, digit1_interval + 1):
    if d1 % 2 == 0:
        for d2 in range(1, digit2_interval + 1):
            if d2 == 2 or d2 == 3 or d2 == 5 or d2 == 7:
                for d3 in range(1, digit3_interval + 1):
                    if d3 % 2 == 0:
                        print(f'{d1} {d2} {d3}', end='\n')

