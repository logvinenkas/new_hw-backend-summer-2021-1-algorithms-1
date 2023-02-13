from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self, start=None, stack=None) -> list[Node]:
        # raise NotImplementedError

        if start is None or stack is None:
            start = self._root
            stack: list = [start]

        for item in start.outbound:
            if item not in stack:
                stack.append(item)
                self.dfs(item, stack)
        return stack

    def bfs(self, vertices=None) -> list[Node]:
        # raise NotImplementedError

        if vertices is None:
            vertices: list = [self._root]

        for item in vertices:
            vertices += [x for x in list(item.outbound) if x not in vertices]
        return vertices
