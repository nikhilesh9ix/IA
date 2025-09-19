def bfs(graph, start):
    visited = set()
    queue = [start]
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            print(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

bfs(graph, 'A')
