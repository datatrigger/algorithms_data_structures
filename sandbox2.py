def f(i: int, j: int) -> bool:
    # Bases cases:
    if i == len(s):
        return (
            j == len(p)
            or (j == len(p) - 2 and p[-1] == "*")
        )
    if (j == len(p)):
        return i == len(s)
    # Recursion
    if s[i] == p[j] or p[j] == ".":
        return f(i + 1, j + 1) or (j + 1 < len(p) and p[j + 1] == "*" and f(i + 1, j))
    return False

s = "aa"
p = "aa"
print(f(0, 0))
    