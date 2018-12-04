

def puzzle1():
    freq = 0
    with open('./data/2018.01.txt', 'r') as _file:
        for line in _file:
            val = line.strip()
            if val[0] == '-':
                freq -= int(val[1:])
            elif val[0] == '+':
                freq += int(val[1:])
    return freq

def puzzle2():
    freq = 0
    freq_set = set()
    steps = []

    with open('./data/2018.01.txt', 'r') as _file:
        steps = list(map(lambda line: line.strip(), _file.readlines()))
    while True:
        for step in steps:
            if step[0] == '-':
                freq -= int(step[1:])
            elif step[0] == '+':
                freq += int(step[1:])
            if freq in freq_set:
                return freq
            freq_set.add(freq)

if __name__ == '__main__':
    print(puzzle1())
    print(puzzle2())
