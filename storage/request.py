from storage.abstract_storage import AbstractStorage
from storage.exceptions import IncorrectInputFormatError, IncorrectStorageError


class Request:
    def __init__(self, request_phrase: str, storages: dict[str, AbstractStorage]):
        split_phrase = request_phrase.lower().split()
        if len(split_phrase) != 7:
            raise IncorrectInputFormatError

        self.amount = int(split_phrase[1])
        self.product = split_phrase[2]
        self.destination = split_phrase[6]
        self.departure = split_phrase[4]

        if self.destination not in storages or self.departure not in storages:
            raise IncorrectStorageError

