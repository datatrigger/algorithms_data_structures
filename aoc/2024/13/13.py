import re
with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

#1
claws = []
claw =  []
for line in lines:
    if not line:
        continue
    coords = [int(coord) for coord in re.findall(r'\d+', line)]
    claw.append(coords)
    if line.startswith("Prize"):
        claws.append(claw)
        claw = []
       
max_val = 100
total = 0
for a, b, p in claws:
    tokens = float("inf")
    for i in range(max_val + 1):
        for j in range(max_val + 1):
            win = (i * a[0] + j * b[0] == p[0]
                and i * a[1] + j * b[1] == p[1])
            if win:
                tokens = min(tokens, i * 3 + j)
    tokens = tokens if tokens < float("inf") else 0
    total += tokens
print(total)

#2
# Each set of button A, button B and prize
# is a system of 2 equations with 2 variables.
# There can be infinitely many solutions, 1 solution or no solution.
# When there is exactly 1 solution,
# Use it only if the solution (i, j) is a tuple of integers.
claws = []
claw =  []
for line in lines:
    if not line:
        continue
    coords = [int(coord) for coord in re.findall(r'\d+', line)]
    claw.append(coords)
    if line.startswith("Prize"):
        claw[-1] = [10000000000000 + coord for coord in claw[-1]]
        claws.append(claw)
        claw = []

total = 0
for a, b, p in claws:
    xa, ya = a
    xb, yb = b
    xp, yp = p
    determinant = (xa * yb) - (ya * xb)
    if determinant == 0.0:
        continue
    i = ((xp * yb) - (yp * xb)) / determinant
    j = ((xa * yp) - (ya * xp)) / determinant
    if i.is_integer() and j.is_integer():
        total += i * 3 + j
print(int(total))