file = open('E:\\Projekte\\2020\\adventofcode2020\\24-days-of-christmas\\day-3\\input.txt', 'r')
lines = file.readlines()

dx = [1, 3, 5, 7, 1]
dy = [1, 1, 1, 1, 2]

mltp = 1


for i in range(len(dx)):
    trees = 0
    x = 0
    y = 0
    
    while y < len(lines):
        
        l = len(lines[y]) - 1
        
        if lines[y][x] == '#':
            trees += 1
        
        # Next x and y
        x = (x + dx[i]) % l
        y = y + dy[i]
    
    mltp *= trees
    print(trees)

print(mltp)