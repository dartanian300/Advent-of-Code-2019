from math import floor

# read file
file = open("1-1.txt", "r")
# parse lines to list (without \n)
lines = file.read().splitlines()

# cast strings as ints
lines = list(map(int, lines))

total = 0
for i in lines:
    total += floor(i / 3) - 2

print("total fuel: ", total)