"""Every template in the cheat sheet must actually work. Run: pytest content/tests"""
from pathlib import Path


def make_list(mod, values):
    head = None
    for v in reversed(values):
        head = mod.ListNode(v, head)
    return head


def to_values(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def test_two_pointers(load):
    m = load("two-pointers")
    assert m.two_sum_sorted([2, 7, 11, 15], 9) == (0, 1)
    assert m.two_sum_sorted([1, 2, 3], 10) is None
    nums = [1, 1, 2, 3, 3]
    k = m.remove_duplicates(nums)
    assert nums[:k] == [1, 2, 3]


def test_sliding_window(load):
    m = load("sliding-window")
    assert m.longest_unique_substring("abcabcbb") == 3
    assert m.longest_unique_substring("bbbbb") == 1
    assert m.longest_unique_substring("") == 0
    assert m.max_sum_fixed_window([1, 4, 2, 10, 2, 3, 1, 0, 20], 4) == 24


def test_prefix_sum(load):
    m = load("prefix-sum")
    p = m.build_prefix([1, 2, 3, 4])
    assert p[3] - p[1] == 5
    assert m.count_subarrays_with_sum([1, 1, 1], 2) == 2
    assert m.count_subarrays_with_sum([1, -1, 0], 0) == 3


def test_hashing(load):
    m = load("hashing")
    assert m.two_sum([3, 2, 4], 6) == (1, 2)
    assert m.two_sum([3, 3], 6) == (0, 1)
    groups = m.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert sorted(sorted(g) for g in groups) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    assert m.longest_consecutive([100, 4, 200, 1, 3, 2]) == 4


def test_intervals(load):
    m = load("intervals")
    assert m.merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert m.merge_intervals([[1, 10], [2, 3]]) == [[1, 10]]
    assert m.min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert m.min_meeting_rooms([[7, 10], [2, 4]]) == 1


def test_binary_search(load):
    m = load("binary-search")
    assert m.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert m.search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert m.search([], 1) == -1
    assert m.min_eating_speed([3, 6, 7, 11], 8) == 4
    assert m.min_eating_speed([30, 11, 23, 4, 20], 5) == 30


def test_monotonic_stack(load):
    m = load("monotonic-stack")
    assert m.daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert m.max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]


def test_fast_slow_pointers(load):
    m = load("fast-slow-pointers")
    head = make_list(m, [1, 2, 3, 4, 5])
    assert not m.has_cycle(head)
    assert m.middle_node(head).val == 3
    assert m.middle_node(make_list(m, [1, 2, 3, 4])).val == 3
    # make 5 → 3
    node = head
    while node.next:
        node = node.next
    node.next = head.next.next
    assert m.has_cycle(head)
    assert m.cycle_start(head) is head.next.next


def test_linked_list_reversal(load):
    m = load("linked-list-reversal")
    assert to_values(m.reverse_list(make_list(m, [1, 2, 3]))) == [3, 2, 1]
    assert m.reverse_list(None) is None
    assert to_values(m.reverse_between(make_list(m, [1, 2, 3, 4, 5]), 2, 4)) == [1, 4, 3, 2, 5]
    assert to_values(m.reverse_between(make_list(m, [3, 5]), 1, 2)) == [5, 3]


def test_tree_dfs(load):
    m = load("tree-dfs")
    T = m.TreeNode
    root = T(3, T(9), T(20, T(15), T(7)))
    assert m.max_depth(root) == 3
    assert m.is_valid_bst(T(2, T(1), T(3)))
    assert not m.is_valid_bst(T(5, T(1), T(4, T(3), T(6))))
    assert m.diameter(T(1, T(2, T(4), T(5)), T(3))) == 3


def test_bfs(load):
    m = load("bfs")
    T = m.TreeNode
    assert m.level_order(T(3, T(9), T(20, T(15), T(7)))) == [[3], [9, 20], [15, 7]]
    assert m.level_order(None) == []
    grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0]]
    assert m.shortest_path_grid(grid, (0, 0), (2, 0)) == 6
    assert m.shortest_path_grid([[0, 1], [1, 0]], (0, 0), (1, 1)) == -1


def test_graph_dfs(load):
    m = load("graph-dfs")
    grid = [list("11000"), list("11000"), list("00100"), list("00011")]
    assert m.num_islands(grid) == 3
    assert m.count_components(5, [[0, 1], [1, 2], [3, 4]]) == 2


def test_topological_sort(load):
    m = load("topological-sort")
    order = m.topo_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    pos = {c: i for i, c in enumerate(order)}
    assert len(order) == 4 and pos[0] < pos[1] < pos[3] and pos[0] < pos[2] < pos[3]
    assert m.topo_order(2, [[1, 0], [0, 1]]) == []


def test_union_find(load):
    m = load("union-find")
    uf = m.UnionFind(4)
    assert uf.union(0, 1) and uf.union(2, 3)
    assert uf.components == 2
    assert not uf.union(1, 0)
    assert m.redundant_connection([[1, 2], [1, 3], [2, 3]]) == [2, 3]


def test_dijkstra(load):
    m = load("dijkstra")
    assert m.network_delay_time([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2
    assert m.network_delay_time([[1, 2, 1]], 2, 2) == -1
    dist = m.dijkstra(3, [(0, 1, 4), (0, 2, 1), (2, 1, 2)], 0)
    assert dist == [0, 3, 1]


def test_heap_top_k(load):
    m = load("heap-top-k")
    assert m.kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert sorted(m.top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert m.merge_sorted_lists([[1, 4, 5], [1, 3, 4], [2, 6], []]) == [1, 1, 2, 3, 4, 4, 5, 6]
    mf = m.MedianFinder()
    mf.add(1)
    mf.add(2)
    assert mf.median() == 1.5
    mf.add(3)
    assert mf.median() == 2


def test_backtracking(load):
    m = load("backtracking")
    assert sorted(m.subsets([1, 2, 3])) == sorted([[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])
    assert len(m.permutations([1, 2, 3])) == 6 == len({tuple(p) for p in m.permutations([1, 2, 3])})
    assert sorted(m.combination_sum([2, 3, 6, 7], 7)) == [[2, 2, 3], [7]]


def test_dp_1d(load):
    m = load("dp-1d")
    assert m.rob_top_down([2, 7, 9, 3, 1]) == 12
    assert m.rob_constant_space([2, 7, 9, 3, 1]) == 12
    assert m.rob_constant_space([]) == 0
    assert m.coin_change([1, 2, 5], 11) == 3
    assert m.coin_change([2], 3) == -1
    assert m.coin_change([1], 0) == 0
    assert m.word_break("leetcode", ["leet", "code"])
    assert not m.word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])


def test_dp_2d(load):
    m = load("dp-2d")
    assert m.longest_common_subsequence("abcde", "ace") == 3
    assert m.edit_distance("horse", "ros") == 3
    assert m.edit_distance("", "abc") == 3
    assert m.can_partition([1, 5, 11, 5])
    assert not m.can_partition([1, 2, 3, 5])


def test_trie(load):
    m = load("trie")
    t = m.Trie()
    t.insert("apple")
    assert t.search("apple")
    assert not t.search("app")
    assert t.starts_with("app")
    t.insert("app")
    assert t.search("app")
    assert not t.starts_with("b")


def test_every_pattern_has_a_tested_template():
    patterns = Path(__file__).resolve().parent.parent / "patterns"
    slugs = {p.name for p in patterns.iterdir() if p.is_dir()}
    tested = {name[len("test_"):].replace("_", "-") for name in globals() if name.startswith("test_")}
    assert slugs <= tested, f"missing tests for: {sorted(slugs - tested)}"
