graph = {
    'a' : ['b', 'c'],
    'b' : ['d'],
    'c' : ['e'],
    'd': [],
    'e' :[]
}
#BFS
#Initialize queue
queue = []
#a b c
def bfs(graph, start):
    queue.append(start)
    while queue:
        current = queue.pop(0)
        print(current)
        for neighbors in graph[current]:
            queue.append(neighbors)


bfs(graph, 'a')