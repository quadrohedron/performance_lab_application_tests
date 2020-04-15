import sys

def fetch_input(path):
    filename = 'Cash{0}.txt'
    res = []
    for i in range(1,6):
        with open(path+'/'+filename.format(i)) as f:
            text = f.read()
        res.append(tuple(map(float, text.strip().split('\n'))))
    return res

def find_maxcust_interval(data):
    vals = []
    for row in zip(*data):
        vals.append(sum(row))
    print(1+vals.index(max(vals)))
    return None

if __name__ == '__main__':
    find_maxcust_interval(fetch_input(sys.argv[1]))

