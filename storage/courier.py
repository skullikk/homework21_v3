from storage.abstract_storage import AbstractStorage
from storage.request import Request


class Courier:
    def __init__(self, request: Request, storages: dict[str, AbstractStorage]):
        self.__request = request
        self.__from = storages[self.__request.departure]
        self.__to = storages[self.__request.destination]

    def pickup(self):
        self.__from.remove(name=self.__request.product, amount=self.__request.amount)
        print(f'Нужное количество есть на {self.__request.departure}')
        print(f'Курьер забрал {self.__request.amount} {self.__request.product} со {self.__request.departure}')
        print(
            f'Курьер везет {self.__request.amount} {self.__request.product} со {self.__request.departure} в {self.__request.destination}')

    def deliver(self):
        self.__to.add(name=self.__request.product, amount=self.__request.amount)
        print(f'Курьер доставил {self.__request.amount} {self.__request.product} в {self.__request.destination}')

    def return_products(self):
        self.__from.add(name=self.__request.product, amount=self.__request.amount)
        print(f'Курьер вернул {self.__request.amount} {self.__request.product} в {self.__request.departure}')



