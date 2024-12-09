import json
import logging
from exceptions import BookAlreadyExistsException, BookNotFoundException, InvalidSearchFieldException, InvalidBookStatusException

# Настроим логирование
logging.basicConfig(filename='library_management.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Library:
    def __init__(self, data_file='data.json'):
        """Конструктор класса Library.
        Инициализирует библиотеку, загружая данные из файла.
        """
        self.data_file = data_file
        self.books = self._load_books()
    
    def _load_books(self):
        """Загружает книги из файла данных.
        Если файл не существует или пуст, возвращает пустой список.
        """
        try:
            # Проверяем, существует ли файл данных
            try:
                with open(self.data_file, 'r', encoding='utf-8') as file:
                    return json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                # Если файл не найден или пустой, возвращаем пустой список
                return []
        except Exception as e:
            logging.error(f"Ошибка при загрузке данных: {e}")
            return []

    def _save_books(self):
        """Сохраняет книги в файл данных."""
        try:
            with open(self.data_file, 'w', encoding='utf-8') as file:
                json.dump(self.books, file, ensure_ascii=False, indent=4)
        except Exception as e:
            logging.error(f"Ошибка при сохранении данных: {e}")
    
    def add_book(self, title: str, author: str, year: int, status: str = "в наличии"):
        """Добавляет книгу в библиотеку.
        Если книга с таким названием и автором уже существует, выбрасывается исключение.
        """
        # Проверяем, не существует ли книга с таким названием и автором
        if any(book['title'] == title and book['author'] == author for book in self.books):
            raise BookAlreadyExistsException(f"Книга '{title}' автором '{author}' уже существует.")
        
        # Генерация нового уникального ID (если ID уже существует, берем следующий максимальный)
        new_id = max([book['id'] for book in self.books], default=0) + 1
        book = {"id": new_id, "title": title, "author": author, "year": year, "status": status}
        self.books.append(book)
        self._save_books()
        logging.info(f"Добавлена книга: {title} автор: {author}")

    def delete_book(self, book_id: int):
        """Удаляет книгу по ID.
        Если книга не найдена, выбрасывается исключение.
        """
        book_to_remove = next((book for book in self.books if book['id'] == book_id), None)
        if not book_to_remove:
            raise BookNotFoundException(f"Книга с ID {book_id} не найдена.")
        
        self.books.remove(book_to_remove)
        self._save_books()
        logging.info(f"Удалена книга с ID {book_id}")

    def search_books(self, field: str, value: str):
        """Ищет книги по полям title, author или year.
        Если указано неверное поле, выбрасывается исключение.
        """
        if field not in ['title', 'author', 'year']:
            raise InvalidSearchFieldException(f"Неверное поле для поиска: {field}")
        
        if value is None:
            return []
        
        result = [book for book in self.books if str(book[field]).lower() == value.lower()]
        return result

    def change_status(self, book_id: int, new_status: str):
        """Меняет статус книги.
        Статус может быть 'в наличии' или 'выдана'.
        """
        if new_status not in ['в наличии', 'выдана']:
            raise InvalidBookStatusException(f"Неверный статус книги: {new_status}")
        
        book_to_update = next((book for book in self.books if book['id'] == book_id), None)
        if not book_to_update:
            raise BookNotFoundException(f"Книга с ID {book_id} не найдена.")
        
        book_to_update['status'] = new_status
        self._save_books()
        logging.info(f"Статус книги с ID {book_id} изменён на '{new_status}'.")

    def get_books(self):
        """Возвращает все книги в библиотеке."""
        return self.books
