import unittest
from library import Library
from exceptions import BookAlreadyExistsException, BookNotFoundException

class TestLibrary(unittest.TestCase):

    def setUp(self):
        # Инициализация библиотеки с тестовыми данными
        self.library = Library('test_data.json')

    def test_add_book(self):
        # Добавляем книгу в библиотеку
        self.library.add_book("Title", "Author", 2021, "в наличии")
        self.assertEqual(len(self.library.books), 1)

    def test_add_duplicate_book(self):
        # Добавляем книгу и пытаемся добавить её снова (должна возникнуть ошибка)
        self.library.add_book("Title", "Author", 2021, "в наличии")
        with self.assertRaises(BookAlreadyExistsException):
            self.library.add_book("Title", "Author", 2021, "в наличии")

    def test_remove_book(self):
        # Добавляем книгу и удаляем её по ID
        self.library.add_book("Title", "Author", 2021, "в наличии")
        book_id = self.library.books[0]['id']
        self.library.remove_book(book_id)
        self.assertEqual(len(self.library.books), 0)

    def test_remove_nonexistent_book(self):
        # Пытаемся удалить несуществующую книгу
        with self.assertRaises(BookNotFoundException):
            self.library.remove_book(999)

if __name__ == '__main__':
    unittest.main()
