movie_budget = float(input())
movie_destination = input()
season = input()
days = int(input())

movie_day_price = 0
total_movie_price_by_destination_and_season = 0

if movie_destination == "Dubai" and season == "Summer" :
    movie_day_price = 40000
    movie_days_price = days * movie_day_price

    total_movie_price_by_destination_and_season = movie_days_price - 0.3 * movie_days_price

elif movie_destination == 'Dubai' and season == "Winter" :
    movie_day_price = 45000
    movie_days_price = days * movie_day_price

    total_movie_price_by_destination_and_season = movie_days_price - 0.3 * movie_days_price

elif movie_destination == "Sofia" and season == "Summer" :
    movie_day_price = 12500
    movie_days_price = days * movie_day_price

    total_movie_price_by_destination_and_season = movie_days_price + 0.25 * movie_days_price

elif movie_destination == 'Sofia' and season == "Winter" :
    movie_day_price = 17000
    movie_days_price = days * movie_day_price

    total_movie_price_by_destination_and_season = movie_days_price + 0.25 * movie_days_price

elif movie_destination == "London" and season == "Summer" :
    movie_day_price = 20250
    movie_days_price = days * movie_day_price

    total_movie_price_by_destination_and_season = movie_days_price

elif movie_destination == 'London' and season == "Winter" :
    movie_day_price = 24000
    movie_days_price = days * movie_day_price

    total_movie_price_by_destination_and_season = movie_days_price

if total_movie_price_by_destination_and_season <= movie_budget:
    print(f"The budget for the movie is enough! "
    f"We have {(movie_budget - total_movie_price_by_destination_and_season):.2f} leva left!")

else:
    print(f"The director needs {(total_movie_price_by_destination_and_season - movie_budget):.2f} leva more!")



