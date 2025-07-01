def dls(graph, node, goal, depth, path):
    if depth == 0 and node == goal:
        return path + [node]
    if depth > 0:
        for neighbor in graph.get(node, []):
            result = dls(graph, neighbor, goal, depth - 1, path + [node])
            if result:
                return result
    return None

def ids(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        result = dls(graph, start, goal, depth, [])
        if result:
            return result
    return None

# Example
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': ['F'],
    'F': []
}
print(ids(graph, 'A', 'F', 5))
