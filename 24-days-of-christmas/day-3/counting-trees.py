file = open('input.txt', 'r')
lines = file.readlines()

x = 0
dx = 3

trees = 0
l = len(lines[0]) - 1

for line in lines:
    if line[x] == '#':
        trees += 1
    x = (x + dx) % l

print(trees)

"""
..##....#.##...#..#.##....##..#O
#.O..#..#...#.......#...#......
...#....#.#...##......#.#...##.
"""