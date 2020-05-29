import sys


def getMSTWeight(self, parent):
    weight = 0
    for i in range(1, len(self)):
        weight += self[i][parent[i]]
    return weight
    # A utility function to find the MST weight


# minimum distance value, from the set of vertices
# not yet included in shortest path tree
def minKey(self, key, mstSet):
    # Initilaize min value
    min = sys.maxsize
    min_index = None

    for v in range(len(self)):
        if key[v] < min and mstSet[v] is False:
            min = key[v]
            min_index = v

    return min_index


def primMST(self):
    # Key values used to pick minimum weight edge in cut
    key = [sys.maxsize] * len(self)
    parent = [None] * len(self)  # Array to store constructed MST
    # Make key 0 so that this vertex is picked as first vertex
    key[0] = 0
    mstSet = [False] * len(self)

    parent[0] = -1  # First node is always the root

    for cout in range(len(self)):
        # Pick the minimum distance vertex from
        # the set of vertices not yet processed.
        # u is always equal to src in first iteration
        u = minKey(self, key, mstSet)
        if u is None:
            continue
        # Put the minimum distance vertex in
        # the shortest path tree
        mstSet[u] = True

        # Update dist value of the adjacent vertices
        # of the picked vertex only if the current
        # distance is greater than new distance and
        # the vertex in not in the shotest path tree
        for v in range(len(self)):
            # graph[u][v] is non zero only for adjacent vertices of m
            # mstSet[v] is false for vertices not yet included in MST
            # Update the key only if graph[u][v] is smaller than key[v]
            if self[u][v] >= 0 and mstSet[v] is False and key[v] > self[u][v]:
                key[v] = self[u][v]
                parent[v] = u
    if any(v is False for v in mstSet):
        return -1
    return getMSTWeight(self, parent)


if __name__ == "__main__":
    results = []
    C, S, E = [int(el) for el in input().split()]

    graph = [[-1]*C for _ in range(C)]
    for _ in range(E):
        C1,C2,P = (int(x) for x in input().split())

        if graph[C1][C2] != -1:
            if P < graph[C1][C2]:
                graph[C1][C2] = P
                graph[C2][C1] = P
        else:
            graph[C1][C2] = P
            graph[C2][C1] = P
    # remove the most expensive offers for every satellite link available
    for _ in range(S):
        max = 0
        for i in range(C):
            for j in range(C):
                if graph[i][j] > max:
                    max = graph[i][j]
                    max_i, max_j = i, j
        graph[max_i][max_j] = 0

    if len(graph) == 0:
        print(-1)
    else:
        print(primMST(graph))