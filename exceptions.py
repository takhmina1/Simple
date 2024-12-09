class BookAlreadyExistsException(Exception):

    """Исключение для случая, когда книга с таким названием и автором уже существует."""
    
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"BookAlreadyExistsException: {self.args[0]}"

class BookNotFoundException(Exception):
    
    """Исключение для случая, когда книга с указанным ID не найдена."""
    
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"BookNotFoundException: {self.args[0]}"

class InvalidSearchFieldException(Exception):

    """Исключение для случая, когда пользователь пытается искать по некорректному полю."""
    
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"InvalidSearchFieldException: {self.args[0]}"

class InvalidBookStatusException(Exception):

    """Исключение для случая, когда статус книги невалиден (не 'в наличии' и не 'выдана')."""
    
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"InvalidBookStatusException: {self.args[0]}"
