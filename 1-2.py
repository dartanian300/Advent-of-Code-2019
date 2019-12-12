from math import floor

# read file
file = open("1-1.txt", "r")
# parse lines to list (without \n)
lines = file.read().splitlines()

# cast strings as ints
lines = list(map(int, lines))


# recursive function to calc fuel
def calc_fuel(fuel):
    required = floor(fuel / 3) - 2
    if required <= 0:
        return 0
    else:
        return required + calc_fuel(required)

# print(calc_fuel(100756))

total = 0
for i in lines:
    total += calc_fuel(i)

print("total fuel: ", total)
