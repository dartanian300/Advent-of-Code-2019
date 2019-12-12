import csv

with open("2-test.txt", "r") as f:
    reader = csv.reader(f)
    codes = list(reader)[0]

codes = list(map(int, codes))
print("codes: ", codes)

for i, code in enumerate(codes):
    if code == 1:
        pos1 = codes[i + 1]
        pos2 = codes[i + 2]
        pos3 = codes[i + 3]
        val1 = codes[pos1]
        val2 = codes[pos2]
        codes[pos3] = val1 + val2
    elif code == 2:
        pos1 = codes[i + 1]
        pos2 = codes[i + 2]
        pos3 = codes[i + 3]
        val1 = codes[pos1]
        val2 = codes[pos2]
        codes[pos3] = val1 * val2
    elif code == 99:
        break
    else:
        print("unknown opcode")
        break
    # print("i: ", i)
    # print("code: ", code)

print("final codes: ", codes)
