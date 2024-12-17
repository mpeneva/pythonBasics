#number of opened browsers
n = int(input())
salary = int(input())

fine = 0
salary_left = salary
for tab in range(1, n+1):
    web_site_name = input()
    if web_site_name == "Facebook":
        fine += 150
        salary_left = salary - fine
        if salary_left <= 0:
            print("You have lost your salary.")
            break
    elif web_site_name == "Instagram":
        fine += 100
        salary_left = salary - fine
        if salary_left <= 0:
            print("You have lost your salary.")
            break
    elif web_site_name == "Reddit":
        fine += 50
        salary_left = salary - fine
        if salary_left <= 0:
            print("You have lost your salary.")
            break
else:
    salary_left = salary - fine
    print(int(salary_left))
