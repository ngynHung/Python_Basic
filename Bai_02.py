def find_max_positive(arr):
    tmp = [x for x in arr if x > 0]
    if len(tmp) > 0:
        return max(tmp)
    else:
        return '*'


def find_min_negative(arr):
    tmp = [x for x in arr if x < 0]
    if len(tmp) > 0:
        return min(tmp)
    else:
        return '*'


if __name__ == '__main__':
    a = []
    n = int(input('n = '))

    for i in range(n):
        a.append(int(input(f'a[{i}] = ')))

    print(a)

    print('Max positive number:', find_max_positive(a))
    print('Min negative number:', find_min_negative(a))