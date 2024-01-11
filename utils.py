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

# Binary search

def validate_binary_search(algo: Callable) -> bool:
    assert not algo([], 1), "Error: empty array"
    assert not algo([1], 2), "Error: 1-element array"
    assert not algo([1, 3, 7, 11, 14, 15, 16, 20], 2), "Error: random array"
    assert not algo([1, 3, 7, 11, 14, 15, 16, 20], 0), "Error: random array"
    assert not algo([1, 3, 7, 11, 14, 15, 16, 20], 21), "Error: random array"
    
    assert algo([1], 1), "Error: 1-element array"
    assert algo([1, 3, 7, 11, 14, 15, 16, 20], 1), "Error: random array"
    assert algo([1, 3, 7, 11, 14, 15, 16, 20], 16), "Error: random array"
    assert algo([1, 3, 7, 11, 14, 15, 16, 20], 20), "Error: random array"

    print(f"{algo.__name__} successfully passed all test cases!")
    return True

def validate_binary_search_duplicates(algo: Callable) -> bool:
    assert algo([], 1) == (-1, -1), "Error: empty array"
    assert algo([1], 1) == (0, 0), "Error: 1-element array"
    assert algo([1], 2) == (-1, -1), "Error: 1-element array"
    assert algo([1, 1 ,1], 1) == (0, 2), "Error: only duplicates"
    assert algo([1, 1, 1], 2) == (-1, -1), "Error: only duplicates"
    assert algo([0, 1, 2, 3, 4, 5], 2) == (2, 2), "Error: array without duplicates"
    assert algo([0, 1, 2, 4, 5], 3) == (-1, -1), "Error: array without duplicates"
    assert algo([0, 0, 1, 2, 2, 2, 3, 3, 5, 5, 5], 2) == (3, 5),"Error: array with duplicates"
    assert algo([0, 0, 1, 2, 2, 2, 3, 3, 5, 5, 5], 4) == (-1, -1),"Error: array with duplicates"

    print(f"{algo.__name__} successfully passed all test cases!")
    return True

def validate_bisect_left(algo: Callable) -> bool:
    assert algo([], 1) == 0, "Error: empty array"
    assert algo([1], 0) == 0, "Error: 1-element array"
    assert algo([1], 1) == 0, "Error: 1-element array"
    assert algo([1], 2) == 1, "Error: 1-element array"
    assert algo([1, 3, 4], 0) == 0, "Error: array without duplicates"
    assert algo([1, 3, 4], 1) == 0, "Error: array without duplicates"
    assert algo([1, 3, 4], 2) == 1, "Error: array without duplicates"
    assert algo([1, 3, 4], 3) == 1, "Error: array without duplicates"
    assert algo([1, 3, 4], 5) == 3, "Error: array without duplicates"
    assert algo([1, 3, 4, 4, 4, 7], 0) == 0, "Error: array with duplicates"
    assert algo([1, 3, 4, 4, 4, 7], 1) == 0, "Error: array with duplicates"
    assert algo([1, 3, 4, 4, 4, 7], 2) == 1, "Error: array with duplicates"
    assert algo([1, 3, 4, 4, 4, 7], 4) == 2, "Error: array with duplicates"
    assert algo([1, 3, 4, 4, 4, 7], 6) == 5, "Error: array with duplicates"
    assert algo([1, 3, 4, 4, 4, 7], 7) == 5, "Error: array with duplicates"
    assert algo([1, 3, 4, 4, 4, 7], 10) == 6, "Error: array with duplicates"

    print(f"{algo.__name__} successfully passed all test cases!")
    return True

def validate_bisect_right(algo: Callable) -> bool:
    assert algo([], 1) == 0, "Error: empty array"
    assert algo([1], 0) == 0, "Error: 1-element array"
    assert algo([1], 1) == 1, "Error: 1-element array"
    assert algo([1], 2) == 1, "Error: 1-element array"
    assert algo([1, 3, 4], 0) == 0, "Error: array without duplicates"
    assert algo([1, 3, 4], 1) == 1, "Error: array without duplicates"
    assert algo([1, 3, 4], 2) == 1, "Error: array without duplicates"
    assert algo([1, 3, 4], 3) == 2, "Error: array without duplicates"
    assert algo([1, 3, 4], 5) == 3, "Error: array without duplicates"
    assert algo([1, 3, 4, 4, 4, 7], 0) == 0, "Error: array with duplicates"
    assert algo([1, 3, 4, 4, 4, 7], 1) == 1, "Error: array with duplicates"
    assert algo([1, 3, 4, 4, 4, 7], 2) == 1, "Error: array with duplicates"
    assert algo([1, 3, 4, 4, 4, 7], 4) == 5, "Error: array with duplicates"
    assert algo([1, 3, 4, 4, 4, 7], 6) == 5, "Error: array with duplicates"
    assert algo([1, 3, 4, 4, 4, 7], 7) == 6, "Error: array with duplicates"
    assert algo([1, 3, 4, 4, 4, 7], 10) == 6, "Error: array with duplicates"

    print(f"{algo.__name__} successfully passed all test cases!")
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
    assert algo(TreeNode(1), 1), "Error: 1-node tree containing value"
    assert algo(list_to_tree([10, 5, 15, 3, 7, 12, 20]), 7), "Error: tree containing value"
    assert algo(list_to_tree([1, None, 3, None, None, None, 4]), 4), "Error: unbalanced tree containing value"
    
    assert not algo(TreeNode(1), 2), "Error: 1-node tree not containing value"
    assert not algo(list_to_tree([10, 5, 15, 3, 7, 12, 20]), 18), "Error: tree not containing value"
    assert not algo(list_to_tree([1, None, 3, None, None, None, 4]), 5), "Error: unbalanced tree not containing value"

    print(f"{algo.__name__} successfully passed all test cases!")
    return True

def validate_insert(algo: Callable) -> bool:
    assert algo(None, 1) == TreeNode(1), "Error: empty tree"
    assert algo(TreeNode(1), 2) == list_to_tree([1, None, 2]), "Error: 1-node tree"
    assert algo(list_to_tree([3, 1, 5]), 7) == list_to_tree([3, 1, 5, None, None, None, 7]), "Error: basic tree"
    assert algo(list_to_tree([1, None, 3, None, None, None, 4]), 7) ==\
        list_to_tree([1, None, 3, None, None, None, 4, None, None, None, None, None, None, None, 7]), "Error: unbalanced tree"

    print(f"{algo.__name__} successfully passed all test cases!")
    return True

def validate_remove(algo: Callable) -> bool:
    assert algo(None, 42) == None, "Error: empty tree"
    assert algo(TreeNode(42), 42) == None, "Error: 1-node tree with value"
    assert algo(TreeNode(42), 0) == TreeNode(42), "Error: 1-node tree without value"
    assert algo(list_to_tree([3, 1, 5]), 5) == list_to_tree([3, 1]), "Error: basic tree with value"
    assert algo(list_to_tree([3, 1, 5]), 55) == list_to_tree([3, 1, 5]), "Error: basic tree without value"
    assert algo(list_to_tree([1, None, 3, None, None, None, 4]), 4) == list_to_tree([1, None, 3]), "Error: unbalanced tree with value"
    assert algo(list_to_tree([1, None, 3, None, None, None, 4]), 44) ==\
        list_to_tree([1, None, 3, None, None, None, 4]), "Error: unbalanced tree with value"

    print(f"{algo.__name__} successfully passed all test cases!")
    return True

test_traversal_tree = list_to_tree([1, 2, 3, 4, 5, None, 7, None, None, 10, 11, None, None, 14])

def validate_dfs_preorder(algo: Callable) -> bool:
    assert algo(test_traversal_tree) == [1, 2, 4, 5, 10, 11, 3, 7, 14]
    print(f"{algo.__name__} successfully passed the test case!")
    return True

def validate_dfs_inorder(algo: Callable) -> bool:
    assert algo(test_traversal_tree) == [4, 2, 10, 5, 11, 1, 3, 14, 7]
    print(f"{algo.__name__} successfully passed the test case!")
    return True

def validate_dfs_postorder(algo: Callable) -> bool:
    assert algo(test_traversal_tree) == [4, 10, 11, 5, 2, 14, 7, 3, 1]
    print(f"{algo.__name__} successfully passed the test case!")
    return True

def validate_bfs(algo: Callable) -> bool:
    assert algo(test_traversal_tree) == [1, 2, 3, 4, 5, 7, 10, 11, 14]
    print(f"{algo.__name__} successfully passed the test case!")
    return True

def validate_bfs_levels(algo: Callable) -> bool:
    assert algo(test_traversal_tree) == {0: [1], 1: [2, 3], 2: [4, 5, 7], 3: [10, 11, 14]}
    print(f"{algo.__name__} successfully passed the test case!")
    return True

# Graphs

## Grids

test_graph = [[0]*4 for _ in range(4)]
test_graph[1][0] = test_graph[1][1] = test_graph[3][1] = test_graph[2][3] = 1

# o o o o
# 1 1 o o
# o 1 1 o
# o o o o

def validate_dfs(algo: Callable) -> bool:
    assert algo(test_graph) == 2
    print(f"{algo.__name__} successfully passed the test case!")
    return True

def validate_bfs(algo: Callable) -> bool:
    assert algo(test_graph) == 6
    print(f"{algo.__name__} successfully passed the test case!")
    return True

## Adjacency lists

def validate_adjacency_list(algo: Callable) -> bool:
    edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]
    adjacency_list = {'A': ['B'], 'B': ['C', 'E'], 'C': ['E'], 'E': ['D'], 'D': []}
    assert algo(edges) == adjacency_list
    print(f"{algo.__name__} successfully passed the test case!")
    return True

adj = {'A': ['B'], 'B': ['C', 'E'], 'C': ['E'], 'E': ['D'], 'D': []}

def validate_dfs_adj(algo: Callable) -> bool:
    assert algo(adj, "A", "E") == 2
    print(f"{algo.__name__} successfully passed the test case!")
    return True

def validate_bfs_adj(algo: Callable) -> bool:
    assert algo(adj, "A", "E") == 2
    print(f"{algo.__name__} successfully passed the test case!")
    return True
