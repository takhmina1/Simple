from library import Library
from exceptions import BookAlreadyExistsException, BookNotFoundException, InvalidSearchFieldException, InvalidBookStatusException

def main():
    library = Library()

    while True:
        print("\nДобро пожаловать в систему управления библиотекой!")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книги")
        print("4. Изменить статус книги")
        print("5. Просмотр всех книг")
        print("6. Выход")

        choice = input("Введите номер операции: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")

            # Добавлена проверка для года
            while True:
                try:
                    year = int(input("Введите год издания: "))
                    if year < 1000 or year > 9999:
                        raise ValueError("Год издания должен быть четырехзначным числом.")
                    break
                except ValueError as e:
                    print(f"Ошибка: {e}")

            # Статус по умолчанию "в наличии", если ничего не введено
            status = input("Введите статус книги (в наличии/выдана): ").strip() or "в наличии"

            try:
                library.add_book(title, author, year, status)
                print("Книга успешно добавлена!")
            except BookAlreadyExistsException as e:
                print(f"Ошибка: {e}")

        elif choice == '2':
            try:
                book_id = int(input("Введите ID книги для удаления: "))
                library.delete_book(book_id)
                print("Книга успешно удалена!")
            except ValueError:
                print("Ошибка: Введите корректный ID книги.")
            except BookNotFoundException as e:
                print(f"Ошибка: {e}")

        elif choice == '3':
            field = input("По какому полю искать? (title, author, year): ")
            if field not in ['title', 'author', 'year']:
                print("Ошибка: Неверное поле для поиска.")
                continue

            value = input("Введите значение для поиска: ")
            try:
                books = library.search_books(field, value)
                if books:
                    print("Найденные книги:")
                    for book in books:
                        print(f"{book['id']}. {book['title']} автор: {book['author']} год: {book['year']} статус: {book['status']}")
                else:
                    print("Книги не найдены.")
            except InvalidSearchFieldException as e:
                print(f"Ошибка: {e}")

        elif choice == '4':
            try:
                book_id = int(input("Введите ID книги для изменения статуса: "))
                new_status = input("Введите новый статус (в наличии/выдана): ").strip()

                if new_status not in ['в наличии', 'выдана']:
                    print("Ошибка: Статус должен быть 'в наличии' или 'выдана'.")
                    continue

                library.change_status(book_id, new_status)
                print("Статус книги изменён!")
            except ValueError:
                print("Ошибка: Введите корректный ID книги.")
            except (BookNotFoundException, InvalidBookStatusException) as e:
                print(f"Ошибка: {e}")

        elif choice == '5':
            books = library.get_books()
            if books:
                print("Все книги в библиотеке:")
                for book in books:
                    print(f"{book['id']}. {book['title']} автор: {book['author']} год: {book['year']} статус: {book['status']}")
            else:
                print("В библиотеке нет книг.")

        elif choice == '6':
            print("До свидания!")
            break

        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()
