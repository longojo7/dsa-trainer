"""Union-Find with path compression and union by size."""


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]   # path compression (halving)
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        """Merge the groups of a and b. Returns False if they were already connected."""
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False                  # this edge would form a cycle
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra              # attach the smaller tree under the bigger
        self.size[ra] += self.size[rb]
        self.components -= 1
        return True


def redundant_connection(edges: list[list[int]]) -> list[int]:
    uf = UnionFind(len(edges) + 1)        # nodes are labeled 1..n
    for a, b in edges:
        if not uf.union(a, b):
            return [a, b]
    return []
