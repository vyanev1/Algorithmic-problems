def turtleSort(original, required):
    i = len(original)-1
    j = i
    while i >= 0:
        if original[i] != required[j]:
            i -= 1
        else:
            popped = original.pop(i)
            required.pop(j)
            i -= 1
            j -= 1
            #print(f"after popping {popped}: {original}, {required}")
    return len(original)


if __name__ == "__main__":
    k = int(input())
    result = []

    for _ in range(k):
        n = int(input())

        original = []
        for _ in range(n):
            original.append(input().strip())

        required = []
        for _ in range(n):
            required.append(input().strip())

        result.append(turtleSort(original, required))

    for stack in result:
        print(stack)