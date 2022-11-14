from storage.courier import Courier
from storage.exceptions import BaseError, TooMuchProductError
from storage.request import Request
from storage.shop import Shop
from storage.store import Store

store = Store(
    items={
        'печеньки': 3,
        'собачки': 4,
        'коробки': 5,
        'пулемет': 10,
    }
)

shop = Shop(
    items={
        'собачки': 2,
        'печеньки': 5,
        'самолет': 1,
        'пароход': 1,

    }
)

storages = {
    'магазин': shop,
    'склад': store,
}


def main():
    global courier
    while True:
        for storage in storages.keys():
            print(f'В {storage} хранится:\n\n{storages[storage].get_items()}\n')

        user_input = input(
            'Введите задание в формате "Доставить 3 собачки из склад в магазин"\n'
            'Или "стоп" для выхода из программы\n')
        if user_input == 'стоп':
            break
        try:
            request = Request(request_phrase=user_input, storages=storages)
            courier = Courier(request=request, storages=storages)
            courier.pickup()
            courier.deliver()
        except BaseError as e:
            print(e.__class__.__name__)
            if e.__class__.__name__ == 'TooMuchProductError':
                courier.return_products()
            print(e.message)


if __name__ == '__main__':
    main()
