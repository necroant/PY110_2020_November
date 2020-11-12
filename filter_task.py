from itertools import count
from random import randint


def iseven(n):
    return n%2 == 0


def pow2(n):
    return n ** 2


def filter_1():
    all_numbers = count(1,1)                        # Последовательность всех натуральных чисел
    # all_even_numbers = count(2, 2)                # Последовательность четных натуральных чисел здорового человека
    all_even_numbers = filter(iseven, all_numbers)  # Последовательность четных натуральных чисел через жопу
    all_even_numbers_pow2 = map(pow2, all_even_numbers)

    n = 10

    for _ in range(n):
        print(next(all_even_numbers_pow2))

    print(f"Получено {n} элементов")

    for _ in range(n):
        print(next(all_even_numbers_pow2))

    print(f"Получено {n} элементов")


def f1(n):
    return (n % 3 == 0) and n < 0


def filter_2():
    '''
    Из случайного списка
    Найти все отрицательные числа кратные 3
    '''
    n = 100
    random_list = [randint(-100, 100) for _ in range(n)]
    print(list(filter(f1, random_list)))


if __name__ == '__main__':
    # filter_1()
    filter_2()
