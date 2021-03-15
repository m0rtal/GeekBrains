from random import randrange


def generate_graph(vertex, ratio=1.0):
    assert 0 < ratio <= 1, "Неправильная часть"
    graph = dict()
    for i in range(vertex):
        graph[i] = set()
        count_edge = randrange(1, int(vertex * ratio))
        while len(graph[i]) < count_edge:
            edge = randrange(0, vertex)
            if edge != i:
                graph[i].add(edge)
    return graph


def depth_first_search(graph, start):
    path = []
    parent = [None for _ in range(len(graph))]
    is_visited = [None for _ in range(len(graph))]

    def dfs(vertex):
        is_visited[vertex] = True
        path.append(vertex)

        for item in graph[vertex]:
            if not is_visited[item]:
                parent[item] = vertex
                dfs(item)
                path.append(vertex)

        else:
            path.append(-vertex)

    dfs(start)
    return parent, path

g = generate_graph(10, 0.5)

for key, value in g.items():
    print(f"Вершина {key} соединена с вершинами {value}")


s = int(input("С какой вершины начать обход? "))
parent, path = depth_first_search(g, s)
print(parent)
print(path)
