from copy import deepcopy
import random

size = 3
field = [['-'] * size for x in range(size)]


def print_field():
    print('Игровое поле')
    nums = list(map(str, range(size)))
    nums.insert(0, ' ')
    r = iter(range(size))
    field_ = deepcopy(field)
    q = [nums, *field_]

    list(map(lambda x: x.insert(0, str(next(r))), field_))
    print("\n".join(list(map(lambda x: " ".join(x), q))))


def check_win(who='x'):
    has_move()
    rows = []
    cols = []
    diagonal_main = False
    diagonal_second = False
    for i in range(size):
        counter = 0
        for j in range(size):
            if field[i][j] == who:
                counter += 1
        if counter == size:
            rows.insert(i, True)
        else:
            rows.insert(i, False)

    for i in range(size):
        counter = 0
        for j in range(size):
            if field[j][i] == who:
                counter += 1
        if counter == size:
            cols.insert(i, True)
        else:
            cols.insert(i, False)
    main_diag = list(map(lambda x: x[field.index(x)], field))
    second_diag = list(map(lambda x: x[(len(field) - 1) - field.index(x)], field))

    counter = 0
    for i in range(size):
        if main_diag[i] == who:
            counter += 1
    if counter == size:
        diagonal_main = True

    counter = 0
    for i in range(size):
        if second_diag[i] == who:
            counter += 1
    if counter == size:
        diagonal_second = True

    if any(cols) or any(rows) or diagonal_main or diagonal_second:
        if who == 'x':
            print_field()
            print('You Win!')
        else:
            print_field()
            print('AI Wins!')
        exit(0)


def ai():
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    if field[x][y] == '-':
        field[x][y] = 'o'
    else:
        ai()


def has_move():
    can_move = list(map(lambda x: '-' in x, filter(lambda x: '-' in x, field)))
    if not can_move:
        print('Ходы закончились. Ничья.')
        exit()


random.seed()
while (True):
    print_field()
    while (True):
        try:
            x, y = map(int, input('Сделайте ход, укажите координаты через пробел:').split())
            if field[x][y] == '-':
                field[x][y] = 'x'
            else:
                print('Клетка занята')
                continue
        except:
            continue
        else:
            break
    check_win()
    ai()
    check_win('o')
