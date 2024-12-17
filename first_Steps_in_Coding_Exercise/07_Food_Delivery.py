chicken_menu_count = int(input())
fish_menu_count = int(input())
vegetarian_menu_count = int(input())

chicken_menu = chicken_menu_count * 10.35
fish_menu = fish_menu_count * 12.40
vegetarian_menu = vegetarian_menu_count * 8.15
dessert = (chicken_menu + fish_menu + vegetarian_menu) * 0.2
delivery = 2.50

total = chicken_menu + fish_menu + vegetarian_menu + dessert + delivery

print(total)