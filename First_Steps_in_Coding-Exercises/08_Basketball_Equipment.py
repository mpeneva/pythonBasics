annual_tax = int(input())

shoes = annual_tax - annual_tax * 0.4
clothes = shoes - shoes * 0.2
ball = 0.25 * clothes
accessories = 0.2 * ball

total = shoes + clothes + ball + accessories +annual_tax
print(total)