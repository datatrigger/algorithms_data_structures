from __future__ import annotations
from enum import Enum

# Input
input_file = "input"
with open(f"{input_file}.txt", "r") as f:
    codes = [line.strip() for line in f.readlines()]

config_num = {
    "7": (0, 0), "8": (0, 1), "9": (0, 2),
    "4": (1, 0), "5": (1, 1), "6": (1, 2),
    "1": (2, 0), "2": (2, 1), "3": (2, 2),
        "0": (3, 1), "A": (3, 2)
    }
config_dir = {
        "^": (0, 1), "A": (0, 2),
    "<": (1, 0), "v": (1, 1), ">": (1, 2)
    }
order_num = {">": 2, "^": 1, "<": 4, "v": 3}
order_dir = {">": 2, "v": 1, "<": 4, "^": 3}

def f_order_num(command: str) -> int:
    return order_num[command]

def f_order_dir(command: str) -> int:
    return order_dir[command]

class KeyPadType(Enum):
    NUM = {"config": config_num, "f_order": f_order_num}
    DIR = {"config": config_dir, "f_order": f_order_dir}

class KeyPad:

    def __init__(self: KeyPad, key_pad_type: KeyPadType) -> None:
        self.state = "A"
        self.config = key_pad_type.value["config"]
        self.f_order = key_pad_type.value["f_order"]

    def hit(self: KeyPad, target: str) -> str:
        r1, c1 = self.config[self.state]
        r2, c2 = self.config[target]
        dr, dc = r2 - r1, c2 - c1
        self.state = target
        return self.make_sequence(dr, dc)
    
    def make_sequence(self: KeyPad, dr: int, dc: int) -> str:
        vertical = "^" if dr < 0 else "v"
        horizontal = "<" if dc < 0 else ">"
        # sequence = list(abs(dr) * vertical + abs(dc) * horizontal)
        sequence = list(abs(dc) * horizontal + abs(dr) * vertical)
        sequence.sort(key=self.f_order)
        return "".join(sequence) + "A"
    
    def type(self: KeyPad, code: str) -> str:
        sequences = ""
        for c in code:
            sequences += self.hit(c)
        return sequences

numkey = KeyPad(KeyPadType.NUM)
dirkey1 = KeyPad(KeyPadType.DIR)
dirkey2 = KeyPad(KeyPadType.DIR)
codes = [
    "029A",
    "980A",
    "179A",
    "456A",
    "379A"
]

def shortest_sequence(code: str) -> str:    
    s1 = numkey.type(code)
    s2 = dirkey1.type(s1)
    s3 = dirkey2.type(s2)
    return s3

def complexity(code: str) -> str:
    sequence = shortest_sequence(code)
    num = int("".join([c for c in code if c.isdigit()]))
    return len(sequence) * num

def complexity2(code: str) -> str:
    sequence = shortest_sequence(code)
    num = int("".join([c for c in code if c.isdigit()]))
    return len(sequence), num

for code in codes:
    print(f"{code}: {complexity2(code)}")

code = "379A"
s1 = numkey.type(code)
print(s1)
s2 = dirkey1.type(s1)
print(s2)
s3 = dirkey2.type(s2)
print(s3)
#print("<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A")