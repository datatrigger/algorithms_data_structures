with open("input.txt", "r") as f:
    m = [list(line.strip()) for line in f.readlines()]

# 1
R, C = len(m), len(m[0])
target = "XMAS"
def get_count(r, c):
    count = 0
    if m[r][c] != target[0]:
        return 0
    deltas = ((0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1))
    for dr, dc in deltas:
        if 0 <= r + (len(target) - 1) * dr < R and 0 <= c + (len(target) - 1) * dc < C:
            s = "".join(
                [m[r + i * dr][c + i * dc] for i in range(len(target))]
                )
            count += int(s == target)
    return count

res1 = sum(get_count(r, c) for r in range(R) for c in range(C))
print(res1)

# 2
def is_xmas(r, c):
    if 1 <= r < R - 1 and 1 <= c < C - 1 and m[r][c] == "A":
        diag = "".join(m[r - 1][c - 1] + m[r][c] + m[r + 1][c + 1])
        antidiag = "".join(m[r + 1][c - 1] + m[r][c] + m[r - 1][c + 1])
        xmas = (
            (diag == "MAS" or diag[::-1] == "MAS")
            and
            (antidiag == "MAS" or antidiag[::-1] == "MAS")
        )
        return xmas
    return False

res2 = sum(int(is_xmas(r, c)) for r in range(R) for c in range(C))
print(res2)