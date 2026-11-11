"""
Graph structure (Assessment 3.3) - Last name: ANTIDO

Vertices: A, N, T, I, D, O
Edges: each letter is joined to the next letter and the letter after that
       A-N, A-T, N-T, N-I, T-I, T-D, I-D, I-O, D-O
"""
from collections import deque

DEFAULT_NAME = "ANTIDO"


class Graph:
    def __init__(self):
        self.adjacency = {}

    def add_edge(self, a, b):
        self.adjacency.setdefault(a, set()).add(b)
        self.adjacency.setdefault(b, set()).add(a)

    def build(self, letters):
        """Algorithm D: build the graph from the letters."""
        for ch in letters:
            self.adjacency.setdefault(ch, set())
        for i in range(len(letters)):
            for step in (1, 2):
                if i + step < len(letters):
                    self.add_edge(letters[i], letters[i + step])
        self.adjacency = {v: sorted(n) for v, n in self.adjacency.items()}

    def bfs(self, start):
        """Algorithm E: breadth-first search using a queue and visited set."""
        visited = {start}
        queue = deque([start])
        order = []
        while queue:
            vertex = queue.popleft()
            order.append(vertex)
            for neighbor in self.adjacency[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order

    def dfs(self, start):
        """Algorithm F: depth-first search using recursion and visited set."""
        order = []
        self._visit(start, set(), order)
        return order

    def _visit(self, vertex, visited, order):
        visited.add(vertex)
        order.append(vertex)
        for neighbor in self.adjacency[vertex]:
            if neighbor not in visited:
                self._visit(neighbor, visited, order)


def run(name=DEFAULT_NAME):
    """Build the graph from the last name and print its traversals."""
    letters = list(dict.fromkeys(c for c in name.upper() if c.isalpha()))
    graph = Graph()
    graph.build(letters)
    print("=== GRAPH ===")
    for vertex, neighbors in graph.adjacency.items():
        print(f"{vertex}: {', '.join(neighbors)}")
    print("BFS:", " -> ".join(graph.bfs(letters[0])))
    print("DFS:", " -> ".join(graph.dfs(letters[0])))


if __name__ == "__main__":
    run()
