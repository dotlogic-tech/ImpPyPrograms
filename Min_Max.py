def minimax(depth, node_index, is_max, scores, max_depth):
    if depth == max_depth:
        return scores[node_index]

    if is_max:
        return max(
            minimax(depth + 1, node_index * 2, False, scores, max_depth),
            minimax(depth + 1, node_index * 2 + 1, False, scores, max_depth)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, scores, max_depth),
            minimax(depth + 1, node_index * 2 + 1, True, scores, max_depth)
        )

# Example
scores = [3, 5, 6, 9, 1, 2, 0, -1]
print(minimax(0, 0, True, scores, 3))
