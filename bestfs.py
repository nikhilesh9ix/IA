def best_first_search(graph, start, end, heuristic):
    queue = [(start, heuristic[start])]
    visited = []
    
    while queue:
        queue.sort()
        current, _ = queue.pop(0)
        
        print("Visited:", current)
        
        if current == end:
            print("Goal reached")
            return
        
        if current not in visited:
            visited.append(current)
            
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append((neighbor, heuristic[neighbor]))

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 5,
    'E': 2,
    'F': 0
}

best_first_search(graph, 'A', 'F', heuristic)
