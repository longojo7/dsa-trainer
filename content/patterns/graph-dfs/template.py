"""Graph DFS: count connected components on a grid and on an edge list."""
from collections import defaultdict


def num_islands(grid: list[list[str]]) -> int:
    rows, cols = len(grid), len(grid[0])
    seen: set[tuple[int, int]] = set()

    def dfs(r: int, c: int) -> None:
        if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != "1" or (r, c) in seen:
            return
        seen.add((r, c))
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(r + dr, c + dc)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in seen:
                count += 1         # a new island; DFS marks all of it
                dfs(r, c)
    return count


def count_components(n: int, edges: list[list[int]]) -> int:
    graph: defaultdict[int, list[int]] = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    seen: set[int] = set()

    def dfs(node: int) -> None:
        stack = [node]             # iterative DFS avoids Python's recursion limit
        while stack:
            cur = stack.pop()
            if cur in seen:
                continue
            seen.add(cur)
            stack.extend(graph[cur])

    count = 0
    for node in range(n):
        if node not in seen:
            count += 1
            dfs(node)
    return count
