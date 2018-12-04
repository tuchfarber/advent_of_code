def check_multiples(string):
    counts = {}
    for char in string:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return set([v for _, v in counts.items() if 2 <= v <= 3])

def puzzle1():
    dubs = []
    trips = []
    with open('./data/2018.02.txt', 'r') as _file:
        for line in _file:
            line = line.strip()
            counts = check_multiples(line)
            if 2 in counts:
                dubs.append(line)
            if 3 in counts:
                trips.append(line)
    return len(dubs) * len(trips)

def is_off_by_one(code, comparison_code):
    errored = False
    for (index, char) in enumerate(code):
        if char != comparison_code[index]:
            if errored:
                return False
            errored = True
    if not errored:
        # Strigs are the same
        return False
    return True

def get_close_codes(codes):
    for (index, code) in enumerate(codes):
        for comparison_code in codes[index:]:
            if is_off_by_one(code, comparison_code):
                return (code, comparison_code)

def puzzle2():
    with open('./data/2018.02.txt', 'r') as _file:
        codes = list(map(lambda line: line.strip(), _file.readlines()))

    close_codes = get_close_codes(codes)
    return ''.join([
        char
        for (index, char)
        in enumerate(close_codes[0])
        if char == close_codes[1][index]
    ])

if __name__ == '__main__':
    print(puzzle1())
    print(puzzle2())
