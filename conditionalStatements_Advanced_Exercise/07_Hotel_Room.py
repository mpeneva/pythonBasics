month = input()
nights_count = int(input())

studio_price = float(0)
app_price = float(0)

if month in ['May', 'October']:
    studio_price = 50
    app_price = 65

    if nights_count > 7:
        studio_price = studio_price - studio_price * 0.05

    if nights_count > 14:
        studio_price = 50
        studio_price = studio_price - studio_price * 0.3
        app_price = app_price - app_price * 0.1

elif month in ['June', 'September']:
    studio_price = 75.20
    app_price = 68.70

    if nights_count > 14:
        studio_price = studio_price - studio_price * 0.2
        app_price = app_price -  app_price * 0.1

elif month in ['July', 'August']:
    studio_price = 76
    app_price = 77

    if nights_count > 14:
        app_price = app_price -  app_price * 0.1

total_studio_price = nights_count * studio_price
total_app_price = nights_count * app_price

print(f"Apartment: {total_app_price:.2f} lv.")
print(f"Studio: {total_studio_price:.2f} lv.")
