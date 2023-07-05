import heapq

# deklarasi graph yang mewakili peta
# dalam bentuk dictionary
graph = {
    'A': {'heuristic': 10, 'neighbors': {'B': 7, 'E': 8}},
    'B': {'heuristic': 8, 'neighbors': {'A': 7, 'C': 2}},
    'C': {'heuristic': 3, 'neighbors': {'B': 2, 'D': 2, 'E': 5, 'F': 1}},
    'D': {'heuristic': 4, 'neighbors': {'E': 6, 'C': 2, 'F': 3}},
    'E': {'heuristic': 9, 'neighbors': {'A': 8, 'C': 5, 'D': 6}},
    'F': {'heuristic': 0, 'neighbors': {'C': 1, 'D': 3}},
}


def greedy_bfs(graph, start, goal):
    visited = set()
    heap = [(graph[start]['heuristic'], start, [start])]
    while heap:
        (h, current_node, path) = heapq.heappop(heap)
        if current_node in visited:
            continue
        visited.add(current_node)
        if current_node == goal:
            return path
        for neighbor, distance in graph[current_node]['neighbors'].items():
            if neighbor not in visited:
                heapq.heappush(
                    heap, (graph[neighbor]['heuristic'], neighbor, path + [neighbor]))
    return None


# Menguji fungsi greedy_bfs
start = 'A'
goal = 'F'

greedy_path = greedy_bfs(graph, start, goal)
if greedy_path:
    print("Greedy Best-First Search path:", greedy_path)
