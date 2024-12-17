from itertools import filterfalse

prime_sum = 0
complex_sum = 0
isPrime = True

command = ''

while command != 'stop':
    command = input()
    isPrime = True
    if command == 'stop':
        print(f"Sum of all prime numbers is: {prime_sum}")
        print(f"Sum of all non prime numbers is: {complex_sum}")
        break
    else:
        number = int(command)
        if number > 1:
            for i in range(2, number):
                if number % i == 0 and number != i:
                    isPrime = False
                    break

            if isPrime:
                prime_sum += number
            else:
                complex_sum += number
        elif number < 0:
            print("Number is negative.")

else:
    print(f"Sum of all prime numbers is: {prime_sum}")
    print(f"Sum of all non prime numbers is: {complex_sum}")