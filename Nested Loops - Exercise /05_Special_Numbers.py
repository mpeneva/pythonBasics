n = int(input())
break_condition = False
if 1 <= n <= 600000:
    for i in range(1111, 10000):
        i_to_str = str(i)
        break_condition = False
        for position, digit in enumerate(i_to_str):
            int_number = int(digit)
            if int_number == 0 or n % int_number != 0 :
                break_condition = True
                break
        if not break_condition:
            print(i_to_str, end= ' ')
