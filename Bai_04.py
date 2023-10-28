import json


def read_file():
    with open('data/data.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def write_file(file):
    with open('data/data.json', 'w', encoding='utf-8') as f:
        json.dump(file, f, ensure_ascii=False, indent=4)


def add(file, id, name):
    e = {
        'ma_nv': id,
        'ten_nv': name
    }
    file.append(e)
    write_file(file)


def delete_id(file, id):
    for e in file:
        if e['ma_nv'] == id:
            file.remove(e)
            write_file(file)
            return True
    return False


def output_employee(e):
    for k, v in e.items():
        if k == 'ma_nv':
            print(f'Id employee: {v}')
        elif k == 'ten_nv':
            print(f'Name employee: {v}')


def output(file):
    for e in file:
        output_employee(e)


def search_name(file, name):
    return [e for e in file if e['ten_nv'].find(name) >= 0 ]


def separate(n):
    print('=' * n)


if __name__ == '__main__':
    #READ FILE
    d = read_file()
    output(d)
    separate(10)

    #SEARCH NAME
    d2 = search_name(d, 'Nguyễn')
    output(d2)

    # ADD EMPLOYEE
    id = int(input('Enter id employee: '))
    name = input('Enter name employee: ')
    add(d, id, name)
    output(d)

    #DELETE
    id = int(input('Enter id: '))
    delete = delete_id(d, id)
    if delete == True:
        output(d)
    elif delete == False:
        print('Can not find id employee !')


