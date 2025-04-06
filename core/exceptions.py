class ParseError(Exception):
    #Ошибка парсинга SQL-запроса
    def __init__(self, message: str, pos: int = None):
        self.pos = pos
        super().__init__(f"Parse error at position {pos}: {message}" if pos else message)

class ValidationError(Exception):
    #Ошибка валидации AST