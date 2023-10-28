def add(dict, word, mean):
    if word not in dict:
        dict[word] = mean


def delete(dict, word):
    for k in dict:
        if k == word:
            del dict[k]
            return


def translate(dict, word):
    for k, v in dict.items():
        if k == word:
            print(f'"{k}" means "{v}" in Vietnamese')
            return
    print('Can not find word !')


def output(dict):
    for k, v in dict.items():
        print(f'{k} -> {v}')
    print(f'Dictionary has {len(dict)} words')


def separate(n):
    print('=' * n)


if __name__ == '__main__':
    dictionary = {
        'hello': 'xin chao',
        'goodbye': 'tam biet',
        'pen': 'but bi'
    }
    output(dictionary)
    add(dictionary, 'hell', 'dia nguc')
    separate(10)
    output(dictionary)
    separate(10)
    delete(dictionary, 'hell')
    output(dictionary)
    translate(dictionary, 'hell')

