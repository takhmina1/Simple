# Система управления библиотекой

Это консольное приложение для управления библиотекой книг.
Приложение позволяет добавлять, удалять, искать и изменять статус книг.

# Функционал
# Добро пожаловать в систему управления библиотекой!
# 1. Добавить книгу
# 2. Удалить книгу
# 3. Искать книги
# 4. Изменить статус книги
# 5. Просмотр всех книг
# 6. Выход


# Запуск

1. git clone 
2. Запустите `main.py` для взаимодействия с библиотекой через консоль.


# python3 main.py


# Введите номер операции: 1
# Введите название книги: Шум и ярость
# Введите автора книги: Уильям Фолкнер
# Введите год издания: 1929
# Введите статус книги (в наличии/выдана): выдана  



# Введите номер операции: 2
# Введите ID книги для удаления: 3
# Книга успешно удалена!



# Введите номер операции: 3
# По какому полю искать? (title, author, year): title
# Введите значение для поиска: Война и мир

# Найденные книги:
# 1. Война и мир автор: Лев Толстой год: 1869 статус: в наличии

# Книги не найдены.



# Введите номер операции: 4
# Введите ID книги для изменения статуса: 2
# Введите новый статус (в наличии/выдана): выдана
# Ошибка: BookNotFoundException: Книга с ID 2 не найдена.




# Введите номер операции: 5
# Все книги в библиотеке:
# 1. Война и мир автор: Лев Толстой год: 1869 статус: в наличии
# 3. Убийство в Восточном экспрессе автор: Агата Кристи год: 1934 статус: в наличии
# 4. Убийство в Восточном экспрессе автор:  Агата Кристи год: 1934 статус: выдана
# 5. Скотный двор автор: V год: 1945 статус: в наличии
# 6. Гордость и предубеждение автор: Джейн Остин год: 1813 статус: выдана
# 7. Мастер и Маргарита автор: Михаил Булгаков год: 1967 статус: в наличии
# 8. Шум и ярость автор: Уильям Фолкнер год: 1929 статус: выдана
# 9. В поисках утраченного времени автор: Марсель Пруст год: 1913 статус: в наличии
# 10. Один день Ивана Денисовича автор:  Александр Солженицын год: 1962 статус: выдана



# 6. Выход
# Введите номер операции: 6
# До свидания!

