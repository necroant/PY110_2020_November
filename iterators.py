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

if __name__ == '__main__':
    map2()
