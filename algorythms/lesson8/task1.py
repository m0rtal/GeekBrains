def handshakes(num: int) -> int:
    if num < 2:
        print("Маловато у вас друзей")
        return 0
    graph = []
    for i in range(num):
        for j in range(num):
            if i != j:
                graph.append((i, j))
    print(graph)
    return len(graph) // 2


print("Рукопожатий на встрече было: ", handshakes(int(input("Сколько друзей встретилось? "))))
