import sys

def fetch_input(path):
    with open(path) as f:
        text = f.read()
    return sorted(map(int, text.strip().split('\n')))

def calc_stats(numbers):
    N = len(numbers)
    #
    for p in (0.9, 0.5):
        true_index = p*(N-1)+1
        index = int(true_index)                             # В задании было неочевидно,
        a, b = numbers[index-1:index+1]                     # какое конкретное определение перцентиля используется,
        print('{:.2f}'.format(a+(true_index-index)*(b-a)))  # определение подобрано по тестовым данным
    #
    print('{:.2f}'.format(numbers[-1]))
    #
    print('{:.2f}'.format(numbers[0]))
    #
    print('{:.2f}'.format(sum(numbers)/N))
    #
    return None

if __name__ == '__main__':
    calc_stats(fetch_input(sys.argv[1]))
