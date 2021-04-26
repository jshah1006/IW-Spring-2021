# Depth-first search
def dfs(node, explored):
    if node not in explored:
        explored.append(node)
        for i in node.neighbors:
            dfs(i, explored)
    
    return explored


# Breadth-first search
def bfs(start, goal):
    explored = []
    queue = []

    initial_path = []
    initial_path.append(start)
    queue.append(initial_path)

    while (len(queue) > 0):
        path = queue.pop(0)
        temp_node = path[-1]
        if temp_node not in explored:
            for n in temp_node.neighbors:
                new_path = path.copy()
                new_path.append(n)
                queue.append(new_path)
                if n is goal:
                    return new_path
        explored.append(temp_node)


