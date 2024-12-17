
movie_budget = float(input())
movie_destination = input()
movie_season = input()
movie_days = int(input())

total = 0

if movie_destination == 'Dubai':
    if movie_season == 'Winter':
        total = movie_days * 45000 - movie_days * 45000 * 0.3
    elif movie_season == 'Summer':
        total = movie_days * 40000 - movie_days * 40000 * 0.3
elif movie_destination == 'Sofia':
    if movie_season == 'Winter':
        total = movie_days * 17000 + movie_days * 17000 * 0.25
    elif movie_season == 'Summer':
        total = movie_days * 12500 + movie_days * 12500 * 0.25
elif movie_destination == 'London':
    if movie_season == 'Winter':
        total = movie_days * 24000
    elif movie_season == 'Summer':
        total = movie_days * 20250


if movie_budget >= total:
    print(f"The budget for the movie is enough! We have {(movie_budget - total):.2f} leva left!")
else:
    print(f"The director needs {(total - movie_budget):.2f} leva more!")
