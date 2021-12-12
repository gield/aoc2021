from collections import defaultdict
from typing import Dict, List, Set


with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

graph = defaultdict(lambda: set())
for n1, n2 in [tuple(l.split("-")) for l in lines]:
    graph[n1].add(n2)
    graph[n2].add(n1)


def dfs(graph: Dict[str, Set[str]], current_node: str, current_path: List[str]):
    current_path += [current_node]
    if current_node == "end":
        return [current_path]

    paths = []
    small_nodes_in_path = [node for node in current_path if node.islower()]
    can_visit_small_twice = len(small_nodes_in_path) == len(set(small_nodes_in_path))
    for next_node in graph[current_node]:
        if next_node == "start":
            continue
        if next_node.isupper() or next_node not in current_path or can_visit_small_twice:
            for p in dfs(graph, next_node, current_path.copy()):
                paths.append(p)
    return paths


print(len(dfs(graph, "start", [])))
