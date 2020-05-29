def num_of_carries(n1, n2):
    if len(n1) > len(n2):
        n1, n2 = n2, n1
    length = len(n2)

    n1 = n1[::-1]
    n2 = n2[::-1]

    counter = 0
    carry = 0
    for i in range(length):
        if i >= len(n1):
            if int(n2[i]) + carry >= 10:
                counter += 1
                carry = 1
            else:
                carry = 0
        else:
            if int(n1[i]) + int(n2[i]) + carry >= 10:
                counter += 1
                carry = 1
            else:
                carry = 0

    return counter


while True:
    inp = input().split()
    if inp[0] == "0" and inp[1] == "0":
        break
    a = inp[0]
    b = inp[1]
    result = num_of_carries(a,b)
    if result == 0:
        print("No carry operation.")
    elif result == 1:
        print("1 carry operation.")
    else:
        print(result, "carry operations.")