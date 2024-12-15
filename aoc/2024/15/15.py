input_file = "input"

# 1

# Preprocess
directions = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}


def get_input(input_file):
    with open(f"{input_file}.txt", "r") as f:
        lines = (line.strip() for line in f.readlines())

    m = []
    for line in lines:
        if line == "":
            break
        m.append(list(line))
    
    moves = ""
    for line in lines:
        moves += line
    return m, moves

m, moves = get_input(input_file)
R, C = len(m), len(m[0])

# Move
for r in range(len(m)):
    for c in range(len(m[0])):
        if m[r][c] == "@":
            m[r][c] = "."
            rstart, cstart = r, c

def move_robot(r, c, move):
    dr, dc = directions[move]
    if m[r + dr][c + dc] == ".":
        return r + dr, c + dc #nothing: move
    elif m[r + dr][c + dc] == "#":
        return r, c #wall: don't move
    else: #one or more "O"
        rnei, cnei = r + dr, c + dc
        while True:
            if m[rnei][cnei] == ".":
                rdot, cdot = rnei, cnei
                break
            if m[rnei][cnei] == "#":
                return r, c #boxes then wall: don't move
            rnei, cnei = rnei + dr, cnei + dc
        m[r + dr][c + dc] = "."
        m[rdot][cdot] = "O"
        return r + dr, c + dc #move

def make_all_moves(rstart, cstart, moves):
    r, c = rstart, cstart
    for move in moves:
        r, c = move_robot(r, c, move)

make_all_moves(rstart, cstart, moves)
total = sum(100 * r + c for r in range(R) for c in range(C) if m[r][c] == "O")
print(total)

#2

## Preprocess
m, moves = get_input(input_file)
m2 = []
for r in range(len(m)):
    curr_row = []
    for c in range(len(m[0])):
        if m[r][c] == "@":
            curr_row.append("@")
            curr_row.append(".")
        elif m[r][c] == ".":
            curr_row.append(".")
            curr_row.append(".")
        elif m[r][c] == "#":
            curr_row.append("#")
            curr_row.append("#")
        elif m[r][c] == "O":
            curr_row.append("[")
            curr_row.append("]")
    m2.append(curr_row)
m = m2
R, C = len(m), len(m[0])

for r in range(R):
    for c in range(C):
        if m[r][c] == "@":
            m[r][c] = "."
            rstart, cstart = r, c

## Move
def hmove(r, c, dc):
    # m[r][c + dc] is either "[" or "]"
    cnei = c + dc
    while True:
        if m[r][cnei] == ".":
            cdot = cnei
            break
        if m[r][cnei] == "#":
            return r, c #cannot move
        cnei = cnei + dc
    for i in range(abs(cdot - c)):
        m[r][cdot - i * dc] = m[r][cdot - i * dc - dc]
    return r, c + dc

def can_vmove(r, c, dr, boxes):
    boxes.add((r, c))
    if m[r + dr][c] == "." and m[r + dr][c + 1] == ".":
        return True
    if m[r + dr][c] == "#" or m[r + dr][c + 1] == "#":
        return False
    if m[r + dr][c] == "[":
        return can_vmove(r + dr, c, dr, boxes)
    if m[r + dr][c] == "]":
        left = can_vmove(r + dr, c - 1, dr, boxes)
        if m[r + dr][c + 1] == "[":
            right = can_vmove(r + dr, c + 1, dr, boxes)
            return left and right
        return left
    if m[r + dr][c] == ".":
        return can_vmove(r + dr, c + 1, dr, boxes)
    
def vmove(r, c, dr):
    # m[r][c] is "["
    boxes = set()
    if m[r + dr][c] == "[":
        can_move = can_vmove(r + dr, c, dr, boxes)
    else:
        can_move = can_vmove(r + dr, c - 1, dr, boxes)
    if can_move:
        for rbox, cbox in boxes:
            m[rbox][cbox] = "."
            m[rbox][cbox + 1] = "."
        for rbox, cbox in boxes:
            m[rbox + dr][cbox] = "["
            m[rbox + dr][cbox + 1] = "]"
        return r + dr, c
    else:
        return r, c

def move_robot(r, c, move):
    dr, dc = directions[move]
    if m[r + dr][c + dc] == ".":
        return r + dr, c + dc
    if m[r + dr][c + dc] == "#":
        return r, c
    if move in "<>":
        return hmove(r, c, dc)
    return vmove(r, c, dr)

make_all_moves(rstart, cstart, moves)
total = sum(100 * r + c for r in range(R) for c in range(C) if m[r][c] == "[")
print(total)

#########
# DEBUG #
#########

from copy import deepcopy
def mtext(r=rstart, c=cstart):
    mcopy = deepcopy(m)
    mcopy[r][c] = "@"
    return "\n".join(["".join(mcopy[row]) for row in range(R)])

def make_moves(moves, rstart=rstart, cstart=cstart, write=False):
    r, c = rstart, cstart
    if write:
        with open("output.txt", "w") as f:
            pass
        with open("output.txt", "a") as f:
            f.write(f"{mtext(r, c)}\n")
            for i, move in enumerate(moves):
                rprev, cprev = r, c
                r, c = move_robot(r, c, move)
                f.write(f"{i + 1}, {move}\n")
                f.write(f"{mtext(r, c)}\n")
    else:
        print(f"{mtext(r, c)}")
        for i, move in enumerate(moves):
            r, c = move_robot(r, c, move)
            print(f"{i + 1}, {move}")
            print(f"{mtext(r, c)}")
    return r, c

# Example
#r, c = make_moves("<^<<<", rstart=rstart, cstart=cstart)