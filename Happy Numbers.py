import sys

def max_cycle_length(n1, n2):
    max_cycles = 0
    map = {}

    for num in range(n1, n2+1):
        cycles = 1
        current = num

        while current != 1:
            if current in map:
                cycles += map[current] - 1
                break
            if current % 2 != 0:
                current = current * 3 + 1
            else:
                current = current / 2
            cycles += 1

        map[num] = cycles
        max_cycles = max(cycles, max_cycles)

    return max_cycles


inputs = sys.stdin.readlines()
start = int(inputs[0])
end = int(inputs[1])
print(start, end, max_cycle_length(start, end))