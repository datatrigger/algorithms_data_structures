# Input
input_file = "input"
with open(f"{input_file}.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

patterns = lines[0].split(", ")
designs = lines[2:]

# 1
cache = {}
def is_possible(design: str):
    if design == "":
        return True
    if design not in cache:
        cache[design] = False
        for pattern in patterns:
            if design.startswith(pattern):
                cache[design] = cache[design] or is_possible(design[len(pattern):])
    return cache[design]

count = sum(1 for design in designs if is_possible(design))
print(count)

# 2
cache = {}
def ways_to_make(design: str):
    if design == "":
        return 1
    if design not in cache:
        cache[design] = 0
        for pattern in patterns:
            if design.startswith(pattern):
                cache[design] += ways_to_make(design[len(pattern):])
    return cache[design]

ways = sum(ways_to_make(design) for design in designs)
print(ways)