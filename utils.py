from __future__ import annotations
from typing import Callable
from dataclasses import dataclass, field
from collections import deque

# Sorting
def validate_sorting(input_algo: Callable) -> bool:
    # Make sure `input_algo` returns the sorted list
    if input_algo([0]) is None:
        def algo(l: list[int]) -> list[int]:
            input_algo(l)
            return l
    else:
        algo = input_algo

    assert algo([]) == [], "Error: Empty list"
    assert algo([1]) == [1], "Error: One-element list"
    assert algo([1, 1, 1]) == [1, 1, 1], "Error: List of duplicates."
    assert algo([1, 2, 3]) == [1, 2, 3], "Error: Sorted list"
    assert algo([1, 1, 1, 2, 2, 2, 2, 3]) == [1, 1, 1, 2, 2, 2, 2, 3], "Error: Sorted list with duplicates"
    assert algo([7, 2, 5, 6, 1, 9]) == [1, 2, 5, 6, 7, 9], "Error: Unsorted list"
    assert algo([7, 2, 1, 6, 1, 9, 5, 2]) == [1, 1, 2, 2, 5, 6, 7, 9], "Error: Unsorted list with duplicates"
    
    print(f"{input_algo.__name__} successfully sorted all test arrays!")
    return True

# Linked lists
@dataclass
class ListNode:
    val: int|None
    next: int = None

    def __str__(self: ListNode) -> str:
        output = "-> "
        curr = self
        while curr:
            output += f"{curr.val} -> "
            curr = curr.next
        return output

def create_llist(vals: list[int]|None) -> ListNode:
    dummy = ListNode(None)
    curr = dummy
    for val in vals:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def check_equal_llist(head1: ListNode|None, head2:ListNode|None) -> bool:
    curr1, curr2 = head1, head2
    while curr1 and curr2:
        if curr1.val != curr2.val:
            return False
        curr1, curr2 = curr1.next, curr2.next
    return not curr1 and not curr2

def validate_reversing(algo: Callable) -> bool:
    assert check_equal_llist(algo(create_llist([])), create_llist([])), "Error: Empty list"
    assert check_equal_llist(algo(create_llist([1, 2])), create_llist([2, 1])), "Error: basic list"
    assert check_equal_llist(algo(create_llist([1, 2, 3])), create_llist([3, 2, 1])), "Error: basic list"

    print(f"{algo.__name__} successfully reversed all test linked lists!")
    return True
    
# Binary trees
@dataclass
class TreeNode:
    val: int
    left: TreeNode = None
    right: TreeNode = None

def tree_to_list(root: TreeNode) -> list[int|None]:
    values = []
    still_has_nodes = True
    queue = deque()
    queue.append(root)

    while still_has_nodes:
        still_has_nodes = False
        for _ in range(len(queue)):
            curr = queue.popleft()
            if curr:
                if curr.left or curr.right:
                    still_has_nodes = True
                queue.append(curr.left)
                queue.append(curr.right)
                values.append(curr.val)
            else:
                queue.append(None)
                queue.append(None)
                values.append(None)
    while len(values) >= 2 and values[-1] is None:
        values.pop()
    return values

def list_to_tree(values: list[int|None]) -> TreeNode:
    if not values:
        values = [None]
    nodes = [None if value is None else TreeNode(value) for value in values]
    for i, node in enumerate(nodes):
        if node:
            left_idx, right_idx = 2 * i + 1, 2 * i + 2
            if left_idx < len(nodes):
                node.left = nodes[left_idx]
            if right_idx < len(nodes):
                node.right = nodes[right_idx]
    return nodes[0]

def validate_search(algo: Callable) -> bool:
    assert not algo(None, 3), "Error: Empty tree"
    assert algo(list_to_tree([1]), 1), "Error: 1-node tree containing value"
    assert algo(list_to_tree([10, 5, 15, 3, 7, 12, 20]), 7), "Error: tree containing value"
    assert algo(list_to_tree([1, None, 3, None, None, None, 4]), 4), "Error: unbalanced tree containing value"
    
    assert not algo(list_to_tree([1]), 2), "Error: 1-node tree not containing value"
    assert not algo(list_to_tree([10, 5, 15, 3, 7, 12, 20]), 18), "Error: tree not containing value"
    assert not algo(list_to_tree([1, None, 3, None, None, None, 4]), 5), "Error: unbalanced tree not containing value"

    print(f"{algo.__name__} successfully passed all test cases!")
    return True

def validate_insert(algo: Callable) -> bool:
    assert algo(list_to_tree([None]), 1) == list_to_tree([1]), "Error: empty tree"
    assert algo(list_to_tree([1]), 2) == list_to_tree([1, None, 2]), "Error: 1-node tree"
    assert algo(list_to_tree([3, 1, 5]), 7) == list_to_tree([3, 1, 5, None, None, None, 7]), "Error: basic tree"
    assert algo(list_to_tree([1, None, 3, None, None, None, 4]), 7) == list_to_tree([1, None, 3, None, None, None, 4, None, None, None, None, None, None, None, 7]), "Error: unbalanced tree"

    print(f"{algo.__name__} successfully passed all test cases!")
    return True