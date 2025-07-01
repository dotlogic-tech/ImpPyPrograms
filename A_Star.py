import heapq

def astar(graph, start, goal, h):
    pq = [(h[start], 0, start, [])]
    visited = set()

    while pq:
        f, g, node, path = heapq.heappop(pq)
        if node in visited:
            continue
        path = path + [node]
        if node == goal:
            return path, g
        visited.add(node)
        for neighbor, cost in graph[node]:
            heapq.heappush(pq, (g + cost + h[neighbor], g + cost, neighbor, path))
    return None

# Example
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 4)],
    'C': [('D', 1)],
    'D': []
}
heuristic = {'A': 5, 'B': 2, 'C': 2, 'D': 0}
print(astar(graph, 'A', 'D', heuristic))
