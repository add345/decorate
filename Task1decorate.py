#Создать декоратор для использования кэша. Т.е. сохранять аргументы и результаты в словарь,
# если вызывается функция с агрументами,
# которые уже записаны в кэше - вернуть результат из кэша, если нет - выполнить функцию.
#Кэш лучше хранить в json.
# Решение, близкое к решению данной задачи было разобрано на семинаре.

import json
from typing import Callable

cache_json_glob = json.dumps([])


def cache(func: Callable):
    def wrapper(*args, **kwargs):

        glob = globals()
        cache_list = json.loads(glob['cache_json_glob'])

        for record in cache_list:
            if record['kwargs'] == kwargs:
                print('Используем кэш...')
                return record['result']

        new_value = {'kwargs': {}, 'result': 0}
        for key in kwargs.keys():
            new_value['kwargs'][key] = kwargs[key]

        new_value['result'] = func(*args, **kwargs)
        cache_list.append(new_value)
        glob['cache_json_glob'] = json.dumps(cache_list)

        return new_value['result']

    return wrapper

@cache
def my_sum(a1: int, a2: int, a3: int):
    result = a1 + a2 + a3
    return result

if __name__ == '__main__':
    print(my_sum(a1=1, a2=1, a3=1))
    print(my_sum(a1=1, a2=2, a3=3))
    print('Кэш: ', cache_json_glob)
    print(my_sum(a1=1, a2=1, a3=1))