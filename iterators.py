from itertools import count

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

    print(list(map(round_, my_floats)))


def round_(a, n=2):
    return round(a,n)

if __name__ == '__main__':
    # map2()
    map3()