from operator import add, getitem
from itertools import repeat


# https://www.notion.so/Map-864870a4d8cf4611a32a240f62042f2b


def map2():
    num_list = [
        "12",
        "14",
        3.1415926,
        5,
        0xFF,
        0b1010101010
    ]
    print(list(map(int, num_list)))


def map3():
    my_floats = [
        4.356345,
        6.0934,
        3.245235,
        9.77545,
        2.164234234,
        8.884234235,
        4.595235346645
    ]

    # print(list(map(round_, my_floats)))                       # встроенный round
    print(list(map(round, my_floats, [2]*len(my_floats))))      # самописный round


def round_(a, n=2):
    return round(a, n)


def map4():
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    # print(list(map(len, list_words)))
    print(list(map(str.upper, list_words)))


def map5():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]

    print(list(map(add, list1, list2)))   # из библиотеки operator
    # если списки разной длины, map отработает столько раз сколько элементов в более коротком списке и ошибки не будет


def map6():
    hnrrrg = [
        [2, 3, 5, 7],
        [11, 13, 17, 19],
        [23, 29],
        [31, 37]
    ]

    # print(list(map(len, hnrrrg)))         # Найти длину каждой последовательностей
    # print(sum(map(len, hnrrrg)))          # Найти общее количество элементов в списке
    print(max(map(len, hnrrrg)))            # Найти размер максимальной последовательности


def index1():
    my_str = "Всем привет"
    my_list = [1, 3, 5]
    # print("".join(map(getitem, [my_str]*len(my_list), my_list)))
    print("".join(map(getitem, repeat(my_str, len(my_list)), my_list)))


if __name__ == '__main__':
    # map2()
    # map3()
    # map4()
    # map5()
    # map6()
    index1()
