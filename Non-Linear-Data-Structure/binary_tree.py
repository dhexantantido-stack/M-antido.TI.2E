r"""
Binary Tree structure (Assessment 3.3) - Last name: ANTIDO

           A
         /   \
        N     T
       / \   /
      I   D O
"""
from collections import deque

DEFAULT_NAME = "ANTIDO"


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def build(self, letters):
        """Algorithm A: build the tree level by level from the letters."""
        self.root = Node(letters[0])
        queue = deque([self.root])
        i = 1
        while queue and i < len(letters):
            current = queue.popleft()
            current.left = Node(letters[i])
            queue.append(current.left)
            i += 1
            if i < len(letters):
                current.right = Node(letters[i])
                queue.append(current.right)
                i += 1

    def bfs(self):
        """Algorithm B: level-order traversal using a queue."""
        order = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            order.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return order

    def dfs(self):
        """Algorithm C: preorder traversal (Root -> Left -> Right)."""
        order = []
        self._visit(self.root, order)
        return order

    def _visit(self, node, order):
        if node is None:
            return
        order.append(node.data)
        self._visit(node.left, order)
        self._visit(node.right, order)


def run(name=DEFAULT_NAME):
    """Build the tree from the last name and print its traversals."""
    letters = list(dict.fromkeys(c for c in name.upper() if c.isalpha()))
    tree = BinaryTree()
    tree.build(letters)
    print("=== BINARY TREE ===")
    print("BFS:", " -> ".join(tree.bfs()))
    print("DFS:", " -> ".join(tree.dfs()))


if __name__ == "__main__":
    run()
