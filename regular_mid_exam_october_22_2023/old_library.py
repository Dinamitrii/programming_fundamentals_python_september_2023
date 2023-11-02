def add_book(bookshelf, book_name):
    if book_name not in bookshelf:
        bookshelf.insert(0, book_name)


def take_book(bookshelf, book_name):
    if book_name in bookshelf:
        bookshelf.remove(book_name)


def swap_books(bookshelf, book1, book2):
    if book1 in bookshelf and book2 in bookshelf:
        index1, index2 = bookshelf.index(book1), bookshelf.index(book2)
        bookshelf[index1], bookshelf[index2] = bookshelf[index2], bookshelf[index1]


def insert_book(bookshelf, book_name):
    if book_name not in bookshelf:
        bookshelf.append(book_name)


def check_book(bookshelf, index):
    if 0 <= index < len(bookshelf):
        return bookshelf[index]


def main():
    bookshelf = input().split("&")
    outputs = []
    while True:
        command = input()
        if command == "Done":
            break
        parts = command.split(" | ")
        action = parts[0]

        if action == "Add Book":
            add_book(bookshelf, parts[1])
        elif action == "Take Book":
            take_book(bookshelf, parts[1])
        elif action == "Swap Books":
            swap_books(bookshelf, parts[1], parts[2])
        elif action == "Insert Book":
            insert_book(bookshelf, parts[1])
        elif action == "Check Book":
            result = check_book(bookshelf, int(parts[1]))
            if result:
                outputs.append(result)

    for output in outputs:
        print(output)
    print(", ".join(bookshelf))


if __name__ == "__main__":
    main()
