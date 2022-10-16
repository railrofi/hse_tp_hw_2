def _min(n):
    minimal = int(n[0])
    for i in range(len(n)):
        if int(n[i]) < minimal:
            minimal = int(n[i])
    return minimal


def _max(n):
    maximal = int(n[0])
    for i in range(len(n)):
        if int(n[i]) > maximal:
            maximal = int(n[i])
    return maximal


def _sum(n):
    s = 0
    for i in range(len(n)):
        s = s + int(n[i])
    return s


def _mult(n):
    m = 1
    for i in range(len(n)):
        m = m * int(n[i])
    return m


def begin():
    file = input('Введите название файла:')
    f = open(file, 'r')
    a = f.read().split()

    choise = int(input('Выберите функцию:\n1 - поиск минимального числа\n2 - поиск максимального числа'
                       '\n3 - сумма всех чисел в файле\n4 - произведение всех чисел в файле\n'))

    if choise == 1:
        print(_min(a))
    elif choise == 2:
        print(_max(a))
    elif choise == 3:
        print(_sum(a))
    elif choise == 4:
        print(_mult(a))
    else:
        print('Такой залупы нет')


if __name__ == '__main__':
    begin()
