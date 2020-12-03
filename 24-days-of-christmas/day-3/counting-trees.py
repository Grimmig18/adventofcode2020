file = open('E:\\Projekte\\2020\\adventofcode2020\\24-days-of-christmas\\day-3\\input.txt', 'r')
lines = file.readlines()

x = 0
# y = 0
dx = 3
# dy = 1
trees = 0


for line in lines:
    l = len(line) - 1

    if line[x] == '#':
        trees += 1

    x = (x + dx) % l

print(trees)

"""
..##....#.##...#..#.##....##..#O
#.O..#..#...#.......#...#......
...#....#.#...##......#.#...##.
"""