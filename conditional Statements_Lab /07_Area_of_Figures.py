from math import pi
figure = input()

if figure == 'square' :
    a = float(input())
    print( f"{a * a : .2f}" )
elif figure == 'rectangle' :
    a = float(input())
    b = float(input())
    print( f"{a * b : .2f}")
elif figure == 'circle':
    r = float(input())
    print(f"{pi * r * r : .2f}")
elif figure == 'triangle':
    c = float(input())
    h = float(input())
    print( f"{(c * h) / 2 : .2f}" )