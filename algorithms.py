# p. 4
def lattice(x: list[int], y: list[int]) -> list[int]:
    n, m = len(x), len(y)
    z = [None] * (n + m)
    hold = 0
    for k in range(n + m):
        for i in range(min(n, k + 1)):
            j = k - i
            if j >= m:
                continue
            hold += x[i] * y[j]
        z[k] = hold % 10
        hold = hold // 10
    return z

x, y = [5, 2], [5]
print(f"lattice({x}, {y}) = {lattice(x, y)}")
x, y = [2], [5]
print(f"lattice({x}, {y})) = {lattice(x, y)}")
x, y = [0, 0, 1], [1]
print(f"lattice({x}, {y}) = {lattice(x, y)}")