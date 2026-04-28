def depth_limited_search(graph, current, goal, limit):
    if current == goal:
        return [current]
    
    if limit <= 0:
        return None  # cutoff
    
    for neighbor in graph.get(current, []):
        result = depth_limited_search(graph, neighbor, goal, limit - 1)
        if result is not None:
            return [current] + result
    
    return None  # failure


# Example graph (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

start = 'A'
goal = 'G'
depth_limit = 3

path = depth_limited_search(graph, start, goal, depth_limit)

if path:
    print("Path found:", path)
else:
    print("No path found within depth limit")