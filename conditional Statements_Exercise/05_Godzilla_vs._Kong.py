movie_budget = float(input())
static_actors_count = int(input())
static_actor_costume_price = float(input())

costume_price = static_actors_count * static_actor_costume_price

if static_actors_count > 150:
    costume_price = costume_price - costume_price * 0.1
else:
    pass

movie_decor = movie_budget * 0.1
total_movie_price = movie_decor + costume_price

if total_movie_price > movie_budget :
    print("Not enough money!")
    print(f"Wingard needs {abs(movie_budget - total_movie_price):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {abs(total_movie_price - movie_budget):.2f} leva left.")
