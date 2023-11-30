### Recursion

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

### Backtracking

#p. 77
def subset_sum(nums: list[int], target: int) -> bool:
    """Returns True if list of positive integers `nums` contains a subset of elements adding up to `target`"""
    if target == 0:
        return True
    if target < 0 or len(nums) == 0: # actually 2nd condition: empty nums AND target != 0
        # But that would be redundant with 1st base case
        return False
    
    x = nums[-1]
    return (
        subset_sum(nums[:-1], target - x)
        or
        subset_sum(nums[:-1], target)
    )

print(f"Subset sum: {subset_sum([3, 1, 10, 2, 3], 7)}")

# Avoid copies of input array nums:
def subset_sum_idx(nums, i, target):
    if target == 0:
        return True
    if target < 0 or i < 0:
        return False
    return (
        subset_sum_idx(nums, i - 1, target - nums[i])
        or
        subset_sum_idx(nums, i - 1, target)
    )

nums = [3, 1, 10, 2, 3]
print(f"Subset sum with indexes: {subset_sum_idx(nums, len(nums) - 1, 7)}")
      
# Can this algorithm be written iteratively?
# Recall this algorithm to build subsets
def build_subsets(nums):
    subsets = [[]]
    for num in nums:
      subsets += [subset + [num] for subset in subsets]
    return subsets

def subset_sum_iter(nums: list[int], target: int) -> bool:
    """Returns True if list of positive integers `nums` contains a subset of elements adding up to `target`"""
    
    if target == 0:
        return True
    if target < 0 or len(nums) == 0:
        return False
    
    sums = [0]
    for number in nums:
        for curr_sum in tuple(sums):
            new_sum = curr_sum + number
            if new_sum == target:
                return True
            sums.append(new_sum)
    return False

print("Subset sum iterative: ",
    subset_sum_iter([3, 1, 10, 2, 3], 7),
    subset_sum_iter([1, 2, 0, 2, 3], 5),
    subset_sum_iter([1, 2, 0, 2, 3], 10),
    subset_sum_iter([1, 2, 3], 6)
)

#p. 79

# Adapt the boolean function to actually build a subset;
def subset_sum_2(nums :list[int], i:int, target: int) -> list[int]|None:
    if target == 0:
        return []
    if target < 0 or i < 0:
        return

    subset_without = subset_sum_2(nums, i - 1, target)
    subset_with = subset_sum_2(nums, i - 1, target - nums[i])
    return subset_with + [nums[i]] if subset_with is not None else subset_without

nums = [3, 1, 10, 2, 3]
print(f"ss2: {subset_sum_2(nums, len(nums) - 1, 7)}")

# Return all subsets with sum target
def subsets_sum(i, subset, target):
    if target == 0:
        subsets.append(subset[:])
        return
    if target < 0 or i < 0:
        return
    subsets_sum(i - 1, subset, target)
    subset.append(nums[i])
    subsets_sum(i - 1, subset, target - nums[i])
    subset.pop()
    return


nums = [3, 1, 10, 2, 3, 5]
subsets = []
subsets_sum(len(nums) - 1, [], 7)
print(f"All subsets: {subsets}")

#p. 80
def is_splittable(s: str) -> bool:
    '''Returns True if string `s` can be split in words'''
    if not s:
        return True
    for i in range(1, len(s) + 1):
        if s[:i] in words and is_splittable(s[i:]):
            return True
    return False

words = set(["both", "earth", "and", "saturn", "spin", "bot", "heart", "hands", "at", "urns", "pin"])
print(f"""'bothearthandsaturnspin' is splittable: {is_splittable('bothearthandsaturnspin')}""")

# Indexed version
# Not useful in Python because slicing immutables creates copies
# https://stackoverflow.com/questions/64871329/does-string-slicing-perform-copy-in-memory
s = "bothearthandsaturnspin"
def is_splittable_idx(i: int) -> bool:
    '''Returns True if string `s` can be split in words'''
    if i == len(s):
        return True
    for j in range(i + 1, len(s) + 1):
        if s[i:j] in words and is_splittable_idx(j):
            return True
    return False

print(f"""'bothearthandsaturnspin' is splittable (index): {is_splittable_idx(0)}""")

def splittable(i :int) -> bool:
    return True if i == len(s) else any([s[i:j] in words and splittable(j) for j in range(i + 1, len(s) + 1)])

print(f"""'bothearthandsaturnspin' is splittable (condensed): {splittable(0)}""")


# p. 88
# Subset sum - like recursive pattern: taking/not taking element at index i 
def lis(prev: int, curr: int) -> int:
    if curr == len(nums):
      return 0
  
    skip = lis(prev, curr + 1)
    prev_num = nums[prev] if prev >= 0 else float("-inf")
    take =  1 + lis(curr, curr + 1) if prev_num < nums[curr] else skip
    return max(skip, take)

nums = [7, 2, 4, 1, 3, 6, 5]
print(lis(prev=-1, curr=0))

# p. 90
# Alternative recursive pattern:
# Recurse on all potential next element of the subsequence 
def lis2(curr: int) -> int:
    curr_num = nums[curr] if curr >= 0 else float("-inf")
    
    best_length = 0
    for i in range(curr + 1, len(nums)):
        if nums[i] > curr_num:
            best_length = max(best_length, lis2(i))
    return 1 + best_length if curr >= 0 else best_length # do not count -inf at index -1

nums = [7, 2, 4, 1, 3, 6, 5]
print(lis2(curr=-1))

### Dynamic Programming

# p. 105

s = "bothearthandsaturnspin"
cache = {}
def is_splittable_memoized(i: int) -> bool:
    '''Returns True if string `s` can be split in words'''
    if i == len(s):
        return True
    
    for j in range(i + 1, len(s) + 1):
        if j not in cache:
            cache[j] = is_splittable_memoized(j)
        if s[i:j] in words and cache[j]:
            return True
    return False

print(f"""'bothearthandsaturnspin' is splittable (memoized): {is_splittable_memoized(0)}""")

# Notice that each subproblem is_splittable(i) depends only on is_splittable(j), j > i
# So fill the cache in reverse order:


def is_splittable_dp(s: str, words: set[str]):
    n = len(s)
    splittables = [False] * len(s) + [True]
    for i in range(n - 1, -1, -1):
        for j in range(i, n + 1):
            if s[i:j] in words and splittables[j]:
                splittables[i] = True
    return splittables[0]

print(f"""'bothearthandsaturnspin' is splittable (DP): {is_splittable_dp(s, words)}""")

# p. 110
def lis_dp1(nums):
  nums = [float("-inf")] + nums
  n = len(nums)
  array = [([None] * n) + [0] for i in range(n + 1)]

  for j in range(n - 1, 0, -1):
     for i in range(j):
        if nums[i] >= nums[j]:
           array[i][j] = array[i][j + 1]
        else:
           array[i][j] = max(array[i][j + 1], 1 + array[j][j + 1])
  print(array)
  return array[0][1]

nums = [7, 2, 4, 1, 3, 6, 5]
print(lis_dp1(nums))