def flipSort(stack):
    operations = []
    for i in range(len(stack)):
        # current sublist = stack[i:]
        # each iteration we find the max element in the current sublist
        # and place it at position i
        # (something like a selection sort)
        sublist = stack[i:]
        maxIndex = sublist.index(max(sublist)) + i

        if maxIndex != i:
            if maxIndex == len(stack) - 1:
                stack[i:] = stack[i:][::-1]
                operations.append(i+1)
            else:
                # move element to the last position
                stack[maxIndex:] = stack[maxIndex:][::-1]
                operations.append(maxIndex+1)
                # move element to i-th position
                stack[i:] = stack[i:][::-1]
                operations.append(i+1)

    if not operations:
        return "0"
    else:
        return " ".join(map(str, operations))+" 0"


if __name__ == '__main__':
    stack = input().strip()
    stacks = []
    while stack != '0':
        stack = stack.split()
        stacks.append(stack)
        stack = input().strip()

    for stack in stacks:
        print(" ".join(stack))
        stack = [int(number) for number in stack]
        print(flipSort(stack))
    print("0")
