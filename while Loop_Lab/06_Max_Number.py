
import sys

userinput = input()
min_number = sys.maxsize

while userinput != 'Stop':
    int_input = int(userinput)

    if int_input <  min_number:
        min_number = int_input
    userinput = input()


print(min_number)

