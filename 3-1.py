# use dictionary to map coordinates
import csv

segments = []  # empty list for dictionaries (1 for each path)
coords = [0,0]  # x/y coordinates

# @param l list<int> - list of length 2
def manhattan_distance(l):
    parts = parse_coord(l)
    s = abs(parts[0]) + abs(parts[1])
    return s

# @param c string - cartesian string to parse. format: "x,y"
def parse_coord(c):
    return list(map(int, c.split(',')))

# returns intersection of 2 lists
def intersection(l1, l2):
    return list(set(l1).intersection(l2))

"""
@param dir string - direction line is going (possible values: 'U', 'D', 'L', 'R')
@param len int - the length of the line (equal to the number of segments it produces)
@param segs Map - the map for which to store the segments
"""
def populate_segments(dir, len, segs):
    c = coords.copy()
    for i in range(0, len):
        # print("-"*10)
        # print("dir: ", dir)
        # print("len: ", len)
        # f = ','.join(map(str, c))  # from
        c = increment_coords(dir, c)
        t = ','.join(map(str, c))  # to
        # print("from: ", f)
        # print("to: ", t)
        segs.append(t)
        # print("coords: ", coords)


def increment_coords(dir, coords=coords, len=1):
    if dir == 'U':
        coords[1] += len
    elif dir == 'D':
        coords[1] -= len
    elif dir == 'R':
        coords[0] += len
    elif dir == 'L':
        coords[0] -= len
    else:
        print("invalid direction code")
        exit()
    return coords


# read file
with open("3.txt", "r") as f:
    reader = csv.reader(f)
    points = list(reader)

print("points: ", points)

# parse into map
for i, point_list in enumerate(points):
    coords = [0,0]
    segments.append([])
    for point in point_list:
        # find direction
        # track direction on grid
        # log in segments
        direction = point[0]
        length = int(point[1:])
        # print("dir: ", direction)
        # print("length: ", length)
        populate_segments(direction, length, segments[i])
        increment_coords(direction, coords, length)


# print("segments: ")
# print(segments[0])
# print(segments[1])

# find intersections
intersections = intersection(segments[0], segments[1])
print("intersections: ", intersections)

# find shortest manhattan distance
shortest = manhattan_distance(intersections[0])
for point in intersections:
    s = manhattan_distance(point)
    if s < shortest:
        shortest = s

print("Shortest Manhattan Distance: ", shortest)





