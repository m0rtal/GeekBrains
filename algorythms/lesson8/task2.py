import math

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]


def dijkstra(graph: list, start: int):
    graph_length = len(graph)
    is_visited = [False] * graph_length
    inf = math.inf
    cost = [inf] * graph_length
    parent = [-1] * graph_length

    cost[start] = 0
    min_cost = 0

    while min_cost < inf:
        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i] and cost[i] > vertex + cost[start]:
                cost[i] = vertex + cost[start]
                parent[i] = start

        min_cost = inf
        for i in range(graph_length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    result = [[] for _ in range(graph_length)]

    for i in range(graph_length):
        if is_visited[i]:
            result[i].append(i)
            j = i
            while parent[j] != -1:
                result[i].append(parent[j])
                j = parent[j]
            result[i].reverse()

    return cost, result


s = int(input("От какой вершины идём? "))
cost, path = dijkstra(g, s)

print(cost)
print(*path, sep="\n")
