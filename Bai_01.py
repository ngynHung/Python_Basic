def square(n):
    for i in range(1, n + 1):
        print('*' * n)


def triangle(n):
    for i in range(1, n + 1):
        print('*' * i)


def triangle_reverse1(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * i)


def triangle_reverse2(n):
    for i in range(n , 0, -1):
        print('*' * i)


def triangle_reverse3(n):
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '*' * i)


def triangle_isosceles(n):
    for i in range(1, n + 1, 2):
        print(('*' * i).center(n))


def separate(n):
    print('=' * n)


if __name__ == '__main__':
    n = -1
    while n <= 0:
        n = int(input('n = '))

    square(n)
    separate(n * 2)

    triangle_isosceles(n)
    separate(n * 2)

    triangle(n)
    separate(n * 2)

    triangle_reverse1(n)
    separate(n * 2)

    triangle_reverse2(n)
    separate(n * 2)

    triangle_reverse3(n)
    separate(n * 2)

