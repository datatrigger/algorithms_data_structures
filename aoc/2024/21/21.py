from __future__ import annotations
from enum import Enum

# Input
input_file = "input"
with open(f"{input_file}.txt", "r") as f:
    codes = [line.strip() for line in f.readlines()]

class KeyPadType(Enum):
    NUM = {
        "7": (0, 0), "8": (0, 1), "9": (0, 2),
        "4": (1, 0), "5": (1, 1), "6": (1, 2),
        "1": (2, 0), "2": (2, 1), "3": (2, 2),
                     "0": (3, 1), "A": (3, 2)
    }
    DIR = {
                 "^": (0, 1), "A": (0, 2),
    "<": (1, 0), "v": (1, 1), ">": (1, 2)
    }

class KeyPad:
    
    def __init__(self, key_pad_type: KeyPadType) -> None:
        self.state = "A"
        self.key_pad_type = key_pad_type
        self.config = key_pad_type.value

    def hit(self, target: str) -> str:
        prev_state = self.state
        self.state = target
        r1, c1 = self.config[prev_state]
        r2, c2 = self.config[target]

        dr, dc = r2 - r1, c2 - c1
        vertical = "^" if dr <= 0 else "v"
        horizontal = "<" if dc <= 0 else ">"
        hfirst = abs(dc) * horizontal + abs(dr) * vertical
        vfirst = abs(dr) * vertical + abs(dc) * horizontal

        if self.key_pad_type == KeyPadType.NUM and prev_state in "147" and target in "0A":
            return [hfirst + "A"]
        elif self.key_pad_type == KeyPadType.NUM and prev_state in "0A" and target in "147":
            return [vfirst + "A"]
        elif self.key_pad_type == KeyPadType.DIR and prev_state in "^A" and target in "<":
            return [vfirst + "A"]
        elif self.key_pad_type == KeyPadType.DIR and prev_state in "<" and target in "^A":
            return [hfirst + "A"]
        else:
            return [hfirst + "A", vfirst + "A"]
    
def shortest_length(code: str, n_directional: int) -> int:
    def dfs(code, n):
        if n == 0:
            return len(code)
        if (code, n) not in cache:
            if n == n_directional + 1:
                keypad = KeyPad(KeyPadType.NUM)
            else:
                keypad = KeyPad(KeyPadType.DIR)
            shortest = 0
            for char in code:
                subshortest = float("inf")
                for subcode in keypad.hit(char): # horizontal or vertical
                    subshortest = min(subshortest, dfs(subcode, n - 1))
                shortest += subshortest
            cache[(code, n)] = shortest
        return cache[(code, n)]
    cache = {}
    return dfs(code, n_directional + 1)

def complexity(code: str, n_directional: int = 2) -> str:
    shortest = shortest_length(code, n_directional)
    num = int("".join([c for c in code if c.isdigit()]))
    return shortest * num

res1 = sum(complexity(code, 2) for code in codes)
print(res1)

res2 = sum(complexity(code, 25) for code in codes)
print(res2)