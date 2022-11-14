from storage.abstract_storage import AbstractStorage
from storage.exceptions import NotEnoughSpaceError, UnknownProductError, NotEnoughProductError


class BaseStorage(AbstractStorage):
    def __init__(self, items: dict[str, int], capacity: int):
        self._items = items
        self._capacity = capacity

    def add(self, name: str, amount: int) -> None:
        if self.get_free_space() < amount:
            raise NotEnoughSpaceError
        self._items[name] = self._items.get(name, 0) + amount

    def remove(self, name: str, amount: int) -> None:
        if name not in self._items:
            raise UnknownProductError

        if self._items[name] < amount:
            raise NotEnoughProductError
        self._items[name] -= amount
        if self._items[name] == 0:
            self._items.pop(name)

    def get_free_space(self) -> int:
        return self._capacity - sum(self._items.values())

    def get_items(self) -> str:
        return '\n'.join([f'{v} {k}' for k, v in self._items.items()])

    def get_unique_items_count(self) -> int:
        return len(self._items)
