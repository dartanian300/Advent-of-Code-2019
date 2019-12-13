import csv

# Read file input
with open("2.txt", "r") as f:
    reader = csv.reader(f)
    codes = list(reader)[0]

codes = list(map(int, codes))
print("codes: ", codes)


# Define function for multiple tests
def test_inputs(noun, verb, codes):
    codes[1] = noun
    codes[2] = verb

    for i, code in enumerate(codes):
        # print("index: ", i)

        # advance 4 entries
        if i != 0 and (i) % 4 != 0:
            continue

        if code == 1:
            # print("opcode: 1")
            pos1 = codes[i + 1]
            pos2 = codes[i + 2]
            pos3 = codes[i + 3]
            val1 = codes[pos1]
            val2 = codes[pos2]
            # print("pos1: ", pos1)
            # print("pos2: ", pos2)
            # print("pos3: ", pos3)
            # print("val1: ", val1)
            # print("val2: ", val2)
            # print("result: ", val1 + val2)
            codes[pos3] = val1 + val2
        elif code == 2:
            # print("opcode: 2")
            pos1 = codes[i + 1]
            pos2 = codes[i + 2]
            pos3 = codes[i + 3]
            val1 = codes[pos1]
            val2 = codes[pos2]
            # print("pos1: ", pos1)
            # print("pos2: ", pos2)
            # print("pos3: ", pos3)
            # print("val1: ", val1)
            # print("val2: ", val2)
            # print("result: ", val1 * val2)
            codes[pos3] = val1 * val2
        elif code == 99:
            # print("opcode: 99")
            break
        else:
            # print("unknown opcode")
            break

    if codes[0] == 19690720:
        print("codes: ", codes)
        return True
    else:
        return False
        # print("")
        # print("codes: ", codes)
        # print("")
        # print("i: ", i)
        # print("code: ", code)


# Prepare inputs
noun = list(range(0, 100))
verb = list(range(0, 100))

# Loop through all possibilities
for n in noun:
    outer = False  # break outer loop when solution found
    for v in verb:
        c = codes.copy()
        if test_inputs(n, v, c):
            print("noun: ", n)
            print("verb: ", v)
            print("final answer (100 * noun + verb): ", 100 * n + v)
            outer = True
            break
    if outer:
        break
