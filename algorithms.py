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


def peasant_iter(x: int, y: int) -> int:
    prod = 0
    while x > 0:
        prod += y if x % 2 else 0
        x, y = x // 2, 2 * y
    return prod

print(peasant_iter(13, 2))

def peasant_rec(x: int, y: int) -> int:
    if x == 0:
        return 0
    
    if x % 2 == 0:
        return peasant_rec(x // 2, 2 * y)
    else:
        return y + peasant_rec(x // 2, 2 * y)

print(peasant_iter(1, 0))
print(peasant_iter(0, 1))
print(peasant_iter(0, 0))
print(peasant_iter(13, 2))
print(peasant_iter(23, 3))

# p. 42

def exp_iter(a, n):
    res = a
    for i in range(n -1):
        res *= a
    return res

print(exp_iter(2, 3))

def exp_rec(a, n):
    if n == 1:
        return a
    res = exp_rec(a, n // 2) * exp_rec(a, n // 2)
    return res if n % 2 == 0 else res * a

print(exp_rec(2, 5)) 

#p. 77
def subset_sum(nums: list[int], target: int) -> bool:
    """Returns True if `nums` contains a subset of elements adding up to `target`"""
    
    if target == 0:
        return True
    if target < 0 or len(nums) == 0: # actually 2nd condition: empty nums AND target != 0
        # But that would be redundant with 1st base case
        return False
    
    x = nums.pop()
    return (
        subset_sum(nums, target - x)
        or
        subset_sum(nums, target)
    )

print(subset_sum([1, 2, 0, 2, 3], 5))