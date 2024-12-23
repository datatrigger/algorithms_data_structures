input_file = "input"
with open(f"{input_file}.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

# Preprocess
a_value = int(lines[0].split(": ")[1])
program = lines[4].split(" ")[1].split(",")
program = [int(instruction) for instruction in program]

# 1
def run(a_value):
    register = {"A": a_value, "B": 0, "C": 0}
    output = []

    # Combo
    def combo(val):
        if not 0 <= val <= 6:
            raise ValueError("Combo operand value is between 0 and 6 included.")
        if 4 <= val <= 6:
            return register[chr(ord("A") + val - 4)]
        return val

    # Functions
    def adv(i):
        register["A"] = int(register["A"] / (2 ** combo(program[i])))
        return i + 1

    def bxl(i):
        register["B"] ^= program[i]
        return i + 1

    def bst(i):
        register["B"] = combo(program[i]) % 8
        return i + 1

    def jnz(i):
        if register["A"] != 0:
            return program[i]
        return i + 1

    def bxc(i):
        register["B"] ^= register["C"]
        return i + 1

    def out(i):
        output.append(combo(program[i]) % 8)
        return i + 1

    def bdv(i):
        register["B"] = int(register["A"] / (2 ** combo(program[i])))
        return i + 1

    def cdv(i):
        register["C"] = int(register["A"] / (2 ** combo(program[i])))
        return i + 1

    f = {
        0: adv,
        1: bxl,
        2: bst,
        3: jnz,
        4: bxc,
        5: out,
        6: bdv,
        7: cdv
    }

    i = 0
    while i + 1 < len(program):
        func = f[program[i]]
        i = func(i + 1)
    return output

output = run(a_value)
print(",".join(map(str, output)))

# 2
# Write down the program with pen and paper.
# The value of A is processed by chunks of 3 bits, starting from "the right",
# then stops when A is truncated down to 0.
# So, try building all sequences of 3-bit numbers that produce the correct output.
# Backtrack when the sequence turns out to be wrong.

def dfs(a_value):
    output = run(a_value)
    if len(output) == len(program):
        if output == program:
            candidates.append(a_value)
        return
    if output != program[-len(output):]:
        return
    for num in range(2 ** 3):
        new_a_value = a_value << 3
        new_a_value |= num
        dfs(new_a_value)

candidates = []
for num in range(2 ** 3):
    dfs(num)
print(min(candidates))
