import sys

def minDistance(graph, dist, sptSet):
    # Initilaize minimum distance for next node
    min = sys.maxsize

    # Search for nearest vertex not in the
    # shortest path tree
    min_index = None
    for v in range(1, len(graph)):
        if dist[v] < min and sptSet[v] is False:
            min = dist[v]
            min_index = v
    return min_index


def minDangRoads(graph):
    n = len(graph)
    
    dist = [sys.maxsize] * n
    parent = [None] * n
    
    dist[1] = 0
    sptSet = [False] * n

    for cout in range(1, n):
        # Pick the minimum distance vertex from
        # the set of vertices not yet processed.
        # u is always equal to src in first iteration
        u = minDistance(graph, dist, sptSet)

        if u is None:   # if there are no more vertices to pick, break the loop
            break

        # Put the minimum distance vertex in the
        # shortest path tree
        sptSet[u] = True

        # Update dist value of the adjacent vertices
        # of the picked vertex only if the current
        # - distance is greater than new distance and
        # - the vertex in not in the shortest path tree
        for v in range(1, n):
            if graph[u][v] >= 0 and sptSet[v] is False and dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]
                parent[v] = u
    path = []
    current = n-1
    while current is not None:
        path.insert(0, current)
        current = parent[current]

    if len(graph) == 1 or dist[n-1] == sys.maxsize:
        return -1
    else:
        return str(dist[n-1]) + " " + str(len(path)-1)


if __name__ == "__main__":
    results = []

    for _ in range(int(input())):
        N, M = [int(el) for el in input().split()]

        adjMatrix = [[-1]*(N+1) for _ in range(N+1)]

        for _ in range(M):
            A, B, T = [int(el) for el in input().split()]
            adjMatrix[A][B] = T
            adjMatrix[B][A] = T

        results.append(minDangRoads(adjMatrix))

    for line in results:
        print(line)