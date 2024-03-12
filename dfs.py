graph = {
    'a' : ['c', 'b'],
    'b' : ['d'],
    'c' : ['e'],
    'd': [],
    'e' :[]
}

#DFS STEPS
#initialize empty stack
# append start to stack
# pop start to current
# loop through currents array and add to stack
# repeat pop to current

stack = []
# FIRST DFS SEARCH ALGO
# def depthFirstSearch(graph, start):
#     stack.append(start)
#     print(stack)
#     while stack:
#         current = stack.pop()
#         print(current)
#         for neighbors in graph[current]:
#             stack.append(neighbors)

# depthFirstSearch(graph, 'a') // a b d c e


#RECURSION DFS
def depthFirstSearch(graph, start):
    stack.append(start)
    print(stack)
    current = stack.pop()
    for neighbors in graph[current]:
        depthFirstSearch(graph, neighbors)

        


depthFirstSearch(graph, 'a') 
# // a c e b d



