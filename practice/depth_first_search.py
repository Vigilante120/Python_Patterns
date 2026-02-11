graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def dfs_iter(graph, start_node):
    visited = set()
    stack = [start_node]

    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)

            for n in reversed(graph[vertex]):
                if n not in visited:
                    stack.append(n)

dfs_iter(graph, 'A')



