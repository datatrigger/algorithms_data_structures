class _DoublyLinkedList:
    class _Node:
        def __init__(self, element, prev = None, next = None):
            self._element = element
            self._prev = prev
            self._next = next
        
    def __init__(self):
        self._header = self._Node(None)
        self._trailer = self._Node(None)
        self._header._next = self._trailer
        self._trailer._prev = self._header

        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self.size == 0

    def _insert_between(self, e, predecessor, successor):
        new_node = self._Node(e, predecessor, successor)
        predecessor._next = new_node
        successor._prev = new_node
        self._size += 1
        return new_node

    def _delete_node(self, node):
        node._prev._next = node._next
        node._next._prev = node._prev
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

# _Node attributes: element, prev, next
# _DoublyLinkedList attributes: header, trailer, size
# _DoublyLinkedList methods: len, is_empty, insert_between(e, pred, succ), delete_node(node)

class PositionalList(_DoublyLinkedList):

    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element
        
        def __eq__(self, other):
            # Checking type of arguments ensures a position and a node cannot be equal
            return type(other) is type(self) and other._node is self._node
        
        def __neq(self, other):
            return not other == self
    
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('Argument p must be of type Position.')
        if p._container is not self:
            raise ValueError('Passed argument p does not belong to current container.')
        if p._node._next is None:
            raise ValueError('Passed argument p is no longer valid.')
        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        input_node = self._validate(p)
        return self._make_position(input_node._prev)

    def after(self, p):
        input_node = self._validate(p)
        return self._make_position(input_node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    # Override inherited version to return Position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        node = self._validate(p)
        return self._insert_between(e, node._prev, node)

    def add_after(self, p, e):
        node = self._validate(p)
        return self._insert_between(e, node, node._next)

    def delete(self, p):
        return self._delete_node(self._validate(p))

    def replace(self, p, e):
        original = self. validate(p)
        old_value = original._element
        original._element = e
        return old_value

L = PositionalList()
L.add_last(7)
L.add_last(2)
L.add_last(3)

def insertion_sort(L):
    current_position = L.after(L.first())
    current_element = current_position.element()
    while current_position is not None:
        walk = L.before(current_position)
        while walk is not None and walk.element() > current_element:
            walk = L.before(walk)
        if walk is None:
            L.add_first(current_element)
        else:
            L.add_after(walk, current_element)
        old_position = current_position
        current_position = L.after(current_position)
        L.delete(old_position)

insertion_sort(L)
