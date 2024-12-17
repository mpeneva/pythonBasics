from math import ceil

days = int(input())
food = float(input())

cat_food_percent = 0
dog_food_percent = 0

cat_food = 0
dog_food = 0

biscuit_count = 0
biscuit_gr = 0

# while days >= 1 :
iterator = 1
while iterator <= days:
    #enter data per day
    dog_food_per_day = int(input())
    cat_food_per_day = int(input())

    cat_food = cat_food + cat_food_per_day
    dog_food = dog_food + dog_food_per_day

    if iterator % 3 == 0 :
        biscuit_count = biscuit_count + 1
        cat_dog_food_per_day = dog_food_per_day + cat_food_per_day
        biscuit_gr = biscuit_gr + cat_dog_food_per_day * 0.1

    else:
        pass
    iterator += 1


total_eaten_food = cat_food + dog_food

print(f"Total eaten biscuits: {round(biscuit_gr)}gr.")
print(f"{((cat_food + dog_food) * 100 / food):.2f}% of the food has been eaten.")
print(f"{(dog_food * 100 / total_eaten_food):.2f}% eaten from the dog.")
print(f"{(cat_food * 100 / total_eaten_food):.2f}% eaten from the cat.")



