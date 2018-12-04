import re

class Cut:
    def __init__(self, claim):
        (
            self.id,
            self.left_margin,
            self.top_margin,
            self.width,
            self.height
        ) = self.extract_cut_data(claim)

    def extract_cut_data(self, claim):
        '''
        Takes claim like: `#1 @ 126,902: 29x28`
        Returns: (claim_id, left_margin, top_margin, width, height)
        '''
        pattern = r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)'
        match = re.match(pattern, claim)
        return (int(group) for group in match.groups())

    def __repr__(self):
        return str((self.id, self.left_margin, self.top_margin, self.width, self.height))

def get_cut_locations(cut):
    locations = []
    for x in range(cut.width):
        for y in range(cut.height):
            location = '{}.{}'.format(x + cut.left_margin, y + cut.top_margin)
            locations.append(location)
    return locations

def get_cuts():
    cuts = []
    with open('./data/2018.03.txt', 'r') as _file:
        for line in _file:
            cuts.append(Cut(line.strip()))
    return cuts

def map_all_cuts(cuts):
    fabric_squares = {} # Will store cuts in {'{x_location}.{y_location}':[{claim_id},]}
    for cut in cuts:
        locations = get_cut_locations(cut)
        for location in locations:
            if location in fabric_squares:
                fabric_squares[location].append(cut.id)
            else:
                fabric_squares[location] = [cut.id]
    return fabric_squares

def puzzle1():
    cuts = get_cuts()
    fabric_squares = map_all_cuts(cuts)
    multiple_cuts = [k for k,v in fabric_squares.items() if len(v) >= 2]
    return len(multiple_cuts)


def puzzle2():
    cuts = get_cuts()
    fabric_squares = map_all_cuts(cuts)
    multiple_cuts = set([k for k,v in fabric_squares.items() if len(v) >= 2])
    for cut in cuts:
        locs = set(get_cut_locations(cut))
        if not locs.intersection(multiple_cuts):
            return cut.id

if __name__ == '__main__':
    print(puzzle1())
    print(puzzle2())
