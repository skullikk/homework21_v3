class BaseError(Exception):
    message = 'Неизвестная ошибка'


class NotEnoughSpaceError(BaseError):
    message = 'Недостаточно места'


class UnknownProductError(BaseError):
    message = 'Нет такого товара'


class NotEnoughProductError(BaseError):
    message = 'Недостаточно товара'


class IncorrectInputFormatError(BaseError):
    message = 'Неправильный формат ввода'


class IncorrectStorageError(BaseError):
    message = 'Неправильное хранилище'


class TooMuchProductError(BaseError):
    message = 'Много товара'
