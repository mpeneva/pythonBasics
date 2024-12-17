# Вход
# От конзолата се прочитат 3 реда, въведени от потребителя:
# N1 - цяло число;
# N2 - цяло число;
# Оператор - един символ измежду: "+", "-", "*", "/", "%".
# Изход
# Да се отпечата на конзолата един ред:
# Ако операцията е събиране, изваждане или умножение:
#  "{N1} {оператор} {N2} = {резултат} - {even/odd}"
# Ако операцията е деление:
# "{N1} / {N2} = {резултат}" - резултат, форматиран до втория знак след десетичната запетая
# Ако операцията е модулно деление:
# "{N1} % {N2} = {остатък}"
# В случай на деление с 0 (нула):
# "Cannot divide {N1} by zero"

number1 = int(input())
number2 = int(input())
operator = input() #+, -, *, /, %

result = float(0)
if operator == "+" :
    result = number1 + number2
    if result % 2 == 0:
        print(f"{number1} + {number2} = {result} - even")
    else:
        print(f"{number1} + {number2} = {result} - odd")
elif operator == "-":
    result = number1 - number2
    if result % 2 == 0:
        print(f"{number1} - {number2} = {result} - even")
    else:
        print(f"{number1} - {number2} = {result} - odd")
elif operator == "*":
    result = number1 * number2
    if result % 2 == 0:
        print(f"{number1} * {number2} = {result} - even")
    else:
        print(f"{number1} * {number2} = {result} - odd")
elif operator == "/":
    if number2 != 0:
        result = number1 / number2
        print(f"{number1} / {number2} = {result:.2f}")
    else:
        print(f"Cannot divide {number1} by zero")
elif operator == "%" :
    if number2 != 0:
        result = number1 % number2
        print(f"{number1} % {number2} = {result}")
    else:
        print(f"Cannot divide {number1} by zero")