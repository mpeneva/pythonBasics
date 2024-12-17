length = int(input())
width = int(input())
height = int(input())

percentage = float(input()) / 100

capacity_total = length * width * height
capacity_net_water = (capacity_total - capacity_total * percentage) / 1000

print(capacity_net_water)
