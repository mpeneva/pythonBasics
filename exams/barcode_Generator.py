# start_number_interval = int(input())
# end_number_interval = int(input())
# break_condition = False
#
#
# for number in range(start_number_interval, end_number_interval +1):
#     number_to_string = str(number)
#     break_condition = False
#     for index, digit in enumerate(number_to_string):
#         if int(digit) % 2 == 0:
#             break_condition = True
#             break
#
#     if break_condition:
#         continue
#     else:
#         print(number, end= ' ')
#####################################################
# from itertools import combinations, permutations, combinations_with_replacement
#
# list_of_digits = []
#
# start_number_interval = input()
# end_number_interval = input()
#
# for i in start_number_interval:
#     if int(i) % 2 != 0:
#         list_of_digits.append(int(i))
#
# for j in end_number_interval:
#     if int(j) % 2 != 0:
#         list_of_digits.append(int(j))
#
#
# print(list_of_digits)
# # result = ''.join(list_of_digits)
# #
# barcodes = combinations_with_replacement(list_of_digits, 4)
#
# for barcode in barcodes:
#     print(barcode, end= ' ')

#################################################
start_number_interval = input()
end_number_interval = input()

a1, a2, a3, a4 = start_number_interval
b1, b2, b3, b4 = end_number_interval

for digit1 in range(int(a1), int(b1)+1):
    for digit2 in range(int(a2), int(b2)+1):
        for digit3 in range(int(a3), int(b3)+1):
            for digit4 in range(int(a4), int(b4)+1):
                if digit1 % 2 !=0 and digit2 % 2 != 0 and digit3 % 2 != 0 and digit4 % 2 != 0:
                    print(f'{digit1}{digit2}{digit3}{digit4}', end= ' ')