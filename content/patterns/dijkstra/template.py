"""Dijkstra's algorithm with heapq and lazy deletion of stale entries."""
import heapq
from collections import defaultdict


def dijkstra(n: int, edges: list[tuple[int, int, int]], source: int) -> list[float]:
    """edges = (u, v, weight), directed. Returns the shortest distance to each node (inf if unreachable)."""
    graph: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))

    dist = [float("inf")] * n
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue                     # stale entry — already found a shorter path
        for nxt, w in graph[node]:
            nd = d + w                   # ← change how cost combines (e.g. max) for variants
            if nd < dist[nxt]:
                dist[nxt] = nd
                heapq.heappush(heap, (nd, nxt))
    return dist


def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    """Nodes are 1..n; time for a signal from k to reach all nodes, or -1."""
    dist = dijkstra(n + 1, [(u, v, w) for u, v, w in times], k)
    worst = max(dist[1:])
    return int(worst) if worst < float("inf") else -1
