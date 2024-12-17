
book_found = input()
book_search = input()
book_counter = 0


while book_search != 'No More Books':
    if book_search == book_found:
        print(f"You checked {book_counter} books and found it.")
        break

    book_search = input()
    book_counter += 1
    continue
else:
    print(f"The book you search is not here!")
    print(f"You checked {book_counter} books.")
