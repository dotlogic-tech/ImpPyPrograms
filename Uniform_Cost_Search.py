import heapq

def ucs(graph, start, goal):
    pq = [(0, start, [])]
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)
        if node in visited:
            continue
        path = path + [node]
        if node == goal:
            return path, cost
        visited.add(node)
        for neighbor, c in graph[node]:
            heapq.heappush(pq, (cost + c, neighbor, path))
    return None

# Example
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('D', 1)],
    'D': []
}
print(ucs(graph, 'A', 'D'))
