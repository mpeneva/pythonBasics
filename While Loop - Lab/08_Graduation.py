student_name = input()
student_avrg_result = 0.0

failed_year_counter = 0
years_counter = 0

while years_counter < 12:

    annual_result = float(input())

    if annual_result < 4:

        failed_year_counter += 1
        if failed_year_counter > 1:
            #failed_year_counter = years_counter + 1
            print(f"{student_name} has been excluded at {(years_counter + 1)} grade")
            break
        continue
    years_counter += 1
    student_avrg_result += annual_result
else:
    avarage_result = student_avrg_result / years_counter
    print(f"{student_name} graduated. Average grade: {avarage_result:.2f}")