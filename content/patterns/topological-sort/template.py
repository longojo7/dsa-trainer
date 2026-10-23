"""Topological sort with Kahn's algorithm (BFS on indegrees)."""
from collections import defaultdict, deque


def topo_order(n: int, prerequisites: list[list[int]]) -> list[int]:
    """prerequisites[i] = [course, prereq]. Returns a valid order, or [] if there's a cycle."""
    graph: defaultdict[int, list[int]] = defaultdict(list)
    indegree = [0] * n
    for course, prereq in prerequisites:
        graph[prereq].append(course)     # edge: prereq → course
        indegree[course] += 1

    queue = deque(i for i in range(n) if indegree[i] == 0)
    order: list[int] = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:       # all its prerequisites are done
                queue.append(nxt)

    return order if len(order) == n else []   # fewer than n → cycle
