import sys

def t_parse(t_string):
    h, m = map(int, t_string.split(':'))
    return 60*h+m

def t_format(t_number):
    h, m = map(str, divmod(t_number, 60))
    if len(m) == 1:
        m = '0'+m
    return h+':'+m

def fetch_input(path):      # Возвращает два списка: времён входа и времён выхода
    enter_times, exit_times = [], []
    with open(path) as f:
        text = f.read()
    for line in text.strip().split('\n'):
        a, b = map(t_parse, line.split(' '))
        enter_times.append(a)
        exit_times.append(b)
    return enter_times, exit_times

def find_maxcust_intervals(enter_times, exit_times):
    temp = {}               # Предварительный словарь для пар время : дельта (изменение числа посетителей)
    for t in enter_times:
        if t in temp:
            temp[t] += 1
        else:
            temp[t] = 1
    for t in exit_times:
        if t in temp:
            temp[t] -= 1
        else:
            temp[t] = -1
    #
    deltas = {}              # Отфильтрованный словарь дельт
    for t in temp:
        v = temp[t]
        if not (v == 0):
            deltas[t] = v
    #
    maxval = 0               # Максимум числа посетителей
    curval = 0               # "Нынешнее" число посетителей по таймлайну
    res = []
    for t, d in sorted(deltas.items(), key = lambda x: x[0]): # Пары сортируются по времени
        if d > 0:
            start_cand = t                                    # Начальная отметка интервала-кандидата
        else:
            if curval == maxval:                              # Если число посетителей равно бывшему максимуму,
                res.append((start_cand, t))                   # новый интервал-кандидат добавляется в список
            elif curval > maxval:                             # Если число посетителей выше бывшего максимума,
                res = [(start_cand, t)]                       # список сбрасывается, добавляется интервал-кандидат,
                maxval = curval                               # а максимум обновляется
        curval += d
    #
    for line in res:
        print(' '.join(tuple(map(t_format, line))))
    #
    return None

if __name__ == '__main__':
    find_maxcust_intervals(*fetch_input(sys.argv[1]))
