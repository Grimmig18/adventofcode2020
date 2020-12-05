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

seat_ids = []

for line in lines:
    line = line.replace('\n', '').replace('\r', '')

    # Get row
    row = binary_tree(line[:7], [0, rows - 1])
    col = binary_tree(line[-3:], [0, columns - 1], lower='L', upper='R')

    seat_ids.append(row * 8 + col)


for seat_id in seat_ids:
    if seat_id + 1 not in seat_ids and seat_id + 2 in seat_ids:
        print(seat_id + 1)
