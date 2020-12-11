file = open('input.txt', 'r')
seat_empty = 'L'
seat_occ = '#'
floor = '.'

seat_map = []

for line in file.readlines(): seat_map.append(line.replace('\n', ''))

def get_adjacent_seats(i, j, seats, seat_empty, seat_occ):
    steps = [
        [1, 0],
        [1, 1],
        [0, 1],
        [-1, 1],
        [-1, 0],
        [-1, -1],
        [0, -1],
        [1, -1]
    ]
    adj = []

    for step in steps:
        i_ = i + step[0]
        j_ = j + step[1]
        while i_ in range(0, len(seats)) and j_ in range(0, len(seats[i])):
            if seats[i_][j_] == seat_occ:
                adj.append(seats[i_][j_])
                break
            elif seats[i_][j_] == seat_empty:
                break

            i_ += step[0]
            j_ += step[1]

    return adj


changes = True
runs = 0

while changes == True:
    new_map = []
    runs += 1

    # Loop through every seat
    i = 0 # Rows
    while i < len(seat_map):
        new_map.append(seat_map[i])
        j = 0 # Seats of row
        while j < len(seat_map[i]):
            # Apply rules
            seat = seat_map[i][j]
            adj = get_adjacent_seats(i, j, seat_map, seat_empty, seat_occ)
            if seat == seat_empty and adj.count(seat_occ) == 0:
                new_map[i] = new_map[i][0:j] + seat_occ + new_map[i][j+1:]
            elif seat == seat_occ and adj.count(seat_occ) >= 5:
                new_map[i] = new_map[i][0:j] + seat_empty + new_map[i][j+1:]

            j += 1
        
        i += 1

    # Check for changes
    i = 0
    changes = False
    while i < len(seat_map):
        if seat_map[i] != new_map[i]:
            changes = True
            break
        i += 1

    seat_map = new_map

occ_count = 0
for row in seat_map:
    occ_count += row.count(seat_occ)
    print(row)

print("Occupied seats: ", occ_count)
print("Runs: ", runs)