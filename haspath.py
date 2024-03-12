graph = {
  "f": ['g', 'i'],
  "g": ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

stack = []

def hasPath(graph, src, dst):
    if src == dst:
            print("True")
            return True
    stack.append(src)
    print(stack)
    curr = stack.pop()
    
        
    for neighbors in graph[curr]:
            if hasPath(graph,neighbors,dst) == True:
                return True
    
    return False

hasPath(graph,'f','j')