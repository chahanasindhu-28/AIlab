from collections import deque

# ----- Graph Definition -----
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# ----- BFS Traversal -----
def bfs(graph, start):
    visited = set()           # To keep track of visited nodes
    queue = deque([start])    # Queue for BFS

    visited.add(start)

    print("BFS Traversal:", end=" ")
    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    print()

# ----- BFS for shortest path distances -----
def bfs_shortest_path(graph, start):
    visited = set([start])
    queue = deque([(start, 0)])  # Store (node, distance from start)

    print("\nBFS Shortest Path Distances:")
    while queue:
        node, dist = queue.popleft()
        print(f"{node} -> Distance: {dist}")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

# ----- Main Program -----
if __name__ == "__main__":
    start_node = 'A'
    bfs(graph, start_node)
    bfs_shortest_path(graph, start_node)