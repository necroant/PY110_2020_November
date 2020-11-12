from itertools import count, zip_longest
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


def zip_1():
    figures = [
        "круг",
        "квадрат",
        "ромб",
        "жо"
    ]

    colors = [
        "красный",
        "белый",
        "коричневый"
    ]

    # for figure, color in zip(figures, colors):
    #     print(f"{figure} цвета {color}")

    """
    если один из списков длиннее другого действует тот же принцип что и с map, не нравится - в библиотеке itertools
    есть функция zip_longest() :
    """

    default_color = "малиновый"

    for figure, color in zip_longest(figures, colors, fillvalue=default_color):
        print(f"{figure} цвета {color}")


def enumerate_2(sequence):
    return zip(range(len(sequence)), sequence)


def parse_matrix():
    matrix = """
        1 2 3
        4 5 6
        7 8 9
        10 11 12
    """

    matrix = matrix.strip()
    matrix = matrix.split('\n')
    matrix = list(map(str.strip, matrix))
    matrix = list(map(str.split, matrix))
    matrix = [list(map(int, sublist)) for sublist in matrix]
    print(matrix)


if __name__ == '__main__':
    # filter_1()
    # filter_2()
    # zip_1()
    # print(list(enumerate_2("Хурма")))
    parse_matrix()
