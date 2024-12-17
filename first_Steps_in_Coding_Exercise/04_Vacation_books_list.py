book_pages_number = int(input())
book_pages_by_hour = int(input())
days_for_book = int(input())

reading_pages_hours = book_pages_number // book_pages_by_hour
reading_hours_per_day = reading_pages_hours // days_for_book

print(reading_hours_per_day)

