from collections import defaultdict

# Input
input_file = "input"
with open(f"{input_file}.txt", "r") as f:
    secrets = [int(line.strip()) for line in f.readlines()]

#1
MOD = 16777216
N = 2000
def nth_number(seed, n):
    curr = seed
    for _ in range(n):
        curr = ((curr * 64) ^ curr) % MOD
        curr = (int(curr / 32) ^ curr) % MOD
        curr = ((curr * 2048) ^ curr) % MOD
    return curr

res1 = sum(nth_number(secret, N) for secret in secrets)
print(res1)

#2

K = 4

def get_prices_and_changes(seed):
    curr = seed
    prices = [curr % 10]
    changes = [None]
    for _ in range(N):
        prev = curr
        curr = ((curr * 64) ^ curr) % MOD
        curr = (int(curr / 32) ^ curr) % MOD
        curr = ((curr * 2048) ^ curr) % MOD
        prices.append(curr % 10)
        changes.append(curr % 10 - prev % 10)
    return prices, changes

def get_max_bananas(secrets):
    bananas = defaultdict(int)
    max_bananas = 0
    for secret in secrets:
        prices, changes = get_prices_and_changes(secret)
        seen = set()
        for i in range(1, len(changes) - K + 1):
            sequence = tuple(changes[i:i + K])
            if sequence in seen:
                continue
            seen.add(sequence)
            bananas[sequence] += prices[i + K - 1]
            max_bananas = max(max_bananas, bananas[sequence])
    return max_bananas

res2 = get_max_bananas(secrets)
print(res2)