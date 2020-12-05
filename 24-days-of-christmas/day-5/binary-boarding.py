file = open('input.txt', 'r')
lines = file.readlines()

rows = 128  # 0 - 127
columns = 8 # 0 - 7
    
def binary_tree(seq, range, lower='F', upper='B'):
    # print(range[0], range[1], seq, lower)
    if range[0] - range[1] == 0:
        return range[0]
    
    if seq[0] == lower:
        range = [range[0], range[1] - ((range[1] - range[0])//2) - 1]
    else:
        range = [range[0] + ((range[1] - range[0])//2) + 1, range[1]]

    return binary_tree(seq[1:], range, lower=lower,)

highest = 0

for line in lines:
    line = line.replace('\n', '').replace('\r', '')

    # Get row
    row = binary_tree(line[:7], [0, rows - 1])
    col = binary_tree(line[-3:], [0, columns - 1], lower='L', upper='R')

    if row * 8 + col > highest:
        highest = row * 8 + col

print(highest)
