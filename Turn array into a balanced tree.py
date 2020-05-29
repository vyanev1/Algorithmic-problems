def buildTree(arr):
    if len(arr) <= 1 and arr[0]:
        tree.append(arr[0])
    elif len(arr) == 2:
        tree.append(arr[1])
        tree.append(arr[0])
    else:
        mid = int(len(arr)/2)
        tree.append(arr[mid])
        tree.append(buildTree(arr[:mid]))
        tree.append(buildTree(arr[mid+1:]))


if __name__ == "__main__":
    result = []
    N = int(input())
    for _ in range(N):
        tree = []
        array = [int(el) for el in input().split()[1:]]
        buildTree(sorted(array))
        result.append(tree)
    for line in result:
        print(" ".join(str(elem) for elem in line if elem))