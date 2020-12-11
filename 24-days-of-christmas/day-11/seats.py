file = open('input.txt', 'r')
seat_empty = 'L'
seat_occ = '#'
floor = '.'

seat_map = []

for line in file.readlines(): seat_map.append(line.replace('\n', ''))

def get_adjacent_seats(i, j, seats):
    adj = []
    # First row
    if i > 0:
        if j > 0 and j < len(seats[i]) - 1:
            adj.extend([seats[i - 1][j-1], seats[i-1][j], seats[i-1][j+1]])
        elif j == 0:
            adj.extend([seats[i-1][j], seats[i-1][j+1]])
        elif j == len(seats[i]) - 1:
            adj.extend([seats[i - 1][j-1], seats[i-1][j]])

    # Second row
    if j > 0 and j < len(seats[i]) - 1:
        adj.extend([seats[i][j-1], seats[i][j+1]])
    elif j == 0:
        adj.extend([seats[i][j+1]])
    elif j == len(seats[i]) - 1:
        adj.extend([seats[i][j-1]])

    # Third Row
    if i < len(seats) - 1:
        if j > 0 and j < len(seats[i]) - 1:
            adj.extend([seats[i + 1][j-1], seats[i+1][j], seats[i+1][j+1]])
        elif j == 0:
            adj.extend([seats[i+1][j], seats[i+1][j+1]])
        elif j == len(seats[i]) - 1:
            adj.extend([seats[i + 1][j-1], seats[i+1][j]])


    return adj


changes = True

while changes == True:
    new_map = []

    # Loop through every seat
    i = 0 # Rows
    while i < len(seat_map):
        new_map.append(seat_map[i])
        j = 0 # Seats of row
        while j < len(seat_map[i]):
            # Apply rules
            seat = seat_map[i][j]
            adj = get_adjacent_seats(i, j, seat_map)
            if seat == seat_empty and adj.count(seat_occ) == 0:
                new_map[i] = new_map[i][0:j] + seat_occ + new_map[i][j+1:]
            elif seat == seat_occ and adj.count(seat_occ) >= 4:
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

print(occ_count)