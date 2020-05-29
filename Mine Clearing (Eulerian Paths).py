def hasEulerianPath(graph):
    for vertex in graph:
        # check outgoing edges
        out_count = 0
        for edge in vertex:
            if edge == 1:
                out_count += 1

        # check incoming edges
        in_count = 0
        for i in range(len(graph)):
            if graph[i][graph.index(vertex)] == 1:
                in_count += 1

        # check if they are equal
        if in_count != out_count:
            return -1

    return 1


if __name__ == "__main__":
    p = int(input())
    for _ in range(p):
        m, n = [int(el) for el in input().split()]
        graph = [[0] * m for i in range(m)]
        for _ in range(n):
            v1, v2 = [int(el) for el in input().split()]
            graph[v1][v2] = 1
            # if edge[0] in graph:
            #     graph[edge[0]].append(edge[1])
            # else:
            #     graph[edge[0]] = [edge[1]]
        print(hasEulerianPath(graph))