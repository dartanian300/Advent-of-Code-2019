import csv

# Read file input
with open("2.txt", "r") as f:
    reader = csv.reader(f)
    codes = list(reader)[0]

codes = list(map(int, codes))
print("codes: ", codes)

codes[1] = 12
codes[2] = 2

# Run Opcodes
for i, code in enumerate(codes):
    print("index: ", i)

    # advance 4 entries
    if i != 0 and (i) % 4 != 0:
        continue

    if code == 1:
        print("opcode: 1")
        pos1 = codes[i + 1]
        pos2 = codes[i + 2]
        pos3 = codes[i + 3]
        val1 = codes[pos1]
        val2 = codes[pos2]
        print("pos1: ", pos1)
        print("pos2: ", pos2)
        print("pos3: ", pos3)
        print("val1: ", val1)
        print("val2: ", val2)
        print("result: ", val1 + val2)
        codes[pos3] = val1 + val2
    elif code == 2:
        print("opcode: 2")
        pos1 = codes[i + 1]
        pos2 = codes[i + 2]
        pos3 = codes[i + 3]
        val1 = codes[pos1]
        val2 = codes[pos2]
        print("pos1: ", pos1)
        print("pos2: ", pos2)
        print("pos3: ", pos3)
        print("val1: ", val1)
        print("val2: ", val2)
        print("result: ", val1 * val2)
        codes[pos3] = val1 * val2
    elif code == 99:
        print("opcode: 99")
        break
    else:
        print("unknown opcode")
        break

    print("")
    print("codes: ", codes)
    print("")
    # print("i: ", i)
    # print("code: ", code)

print("final codes: ", codes)
