# use dictionary to map coordinates
import csv
from map import Map

segments = Map()  # empty dictionary
coords = [0,0]  # x/y coordinates

def populate_segments(dir, len):
    c = coords
    for i in range(0, len):
        print("dir: ", dir)
        print("len: ", len)
        f = ','.join(map(str, c))  # from
        c = increment_coords(dir, c)
        t = ','.join(map(str, c))  # to
        segments.add(f,t)


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



with open("3-test.txt", "r") as f:
    reader = csv.reader(f)
    points = list(reader)

print("points: ", points)

for point in points[0]:
    # find direction
    # track direction on grid
    # log in segments
    direction = point[0]
    length = int(point[1:])
    # print("dir: ", direction)
    # print("length: ", length)
    populate_segments(direction, length)
    increment_coords(direction, coords, length)

print("segments: ", segments)


