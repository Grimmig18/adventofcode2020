file = open('input.txt', 'r')
lines = file.readlines()

visited = []
accumulator = 0

# Instructions: nop, acc, jmp
i = 0

while i not in visited:
    visited.append(i)

    ins = lines[i].split(' ')[0]
    arg = int(lines[i].split(' ')[1])

    if ins == 'acc':
        accumulator += arg
    elif ins == 'jmp':
        i += arg
        continue

    i += 1

print(accumulator)
