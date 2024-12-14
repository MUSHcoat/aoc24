file = open("day2.in",  "r")

def check(arr):
    isSafe = True
    isIncreasing = False
    isDecreasing = False

    for x in arr:
        if 1 <= x <= 3:
            isIncreasing = True
        elif -3 <= x <= -1:
            isDecreasing = True
        else:
            isSafe = False

    if (isIncreasing and isDecreasing) or (not isIncreasing and not isDecreasing):
        isSafe = False        

    return isSafe


def part1():
    ans = 0

    for line in file:
        list = line.split()
        diff = []

        for i in range(1, len(list)):
            diff.append(int(list[i]) - int(list[i - 1]))

        if check(diff):
            ans = ans + 1

    print(ans)

def part2():
    ans = 0

    for line in file:
        list = line.split()
        diff = []

        for i in range(1, len(list)):
            diff.append(int(list[i]) - int(list[i - 1]))

        isDampSafe = False

        for i in range(1, len(diff)):
            aux_arr = diff.copy()
            aux_arr[i] = aux_arr[i] + aux_arr[i - 1]
            aux_arr.pop(i - 1)

            if check(aux_arr):
                isDampSafe = True
        
        aux_arr = diff.copy()
        aux_arr.pop(0)
        if check(aux_arr):
            isDampSafe = True

        aux_arr = diff.copy()
        aux_arr.pop(len(diff) - 1)
        if check(aux_arr):
            isDampSafe = True

        if isDampSafe:
            ans = ans + 1

    print(ans)

part2()