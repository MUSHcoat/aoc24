file = open("day3.in", "r")

mul_beginning = "mul("
do_cmd = "do()"
dont_cmd = "don't()"

def part1():
    ans = 0

    for line in file:
        idx = 0

        while True:
            idx = line.find(mul_beginning, idx)
            if idx == -1:
                break
    
            val1 = 0
            idx = idx + 4
            it = idx
            while line[it].isnumeric():
                val1 = val1 * 10 + int(line[it])
                it = it + 1

            if it - idx > 3:
                idx = it
                continue
            if line[it] != ',':
                idx = it
                continue
        
            val2 = 0
            it = it + 1
            idx = it
            while line[it].isnumeric():
                val2 = val2 * 10 + int(line[it])
                it = it + 1
            
            if it - idx > 3:
                idx = it
                continue
            if line[it] != ')':
                idx = it
                continue

            ans = ans + val1 * val2
            idx = it

    print(ans)

def part2():
    ans = 0
    disabled = False

    for line in file:
        idx = 0

        while True:
            aux = line.find(do_cmd, idx)
            if disabled:
                if aux != -1:
                    disabled = False
                    idx = aux
                    continue
                else:
                    break

            aux = line.find(dont_cmd, idx)
            if not disabled and (aux != -1 and aux < line.find(mul_beginning, idx)):
                disabled = True
                idx = aux
                continue

            if disabled:
                continue

            idx = line.find(mul_beginning, idx)

            if idx == -1:
                break
    
            val1 = 0
            idx = idx + 4
            it = idx
            while line[it].isnumeric():
                val1 = val1 * 10 + int(line[it])
                it = it + 1

            if it - idx > 3:
                idx = it
                continue
            if line[it] != ',':
                idx = it
                continue
        
            val2 = 0
            it = it + 1
            idx = it
            while line[it].isnumeric():
                val2 = val2 * 10 + int(line[it])
                it = it + 1
            
            if it - idx > 3:
                idx = it
                continue
            if line[it] != ')':
                idx = it
                continue

            ans = ans + val1 * val2
            idx = it

    print(ans)

part2()