file = open('input.txt', 'r')
lines = file.readlines()

sum = 0
dict = {}

for line in lines:
    line = line.replace('\n', '')

    # End of group
    if line == '':
        sum += len(dict)
        dict = {}
        # next group
        continue

    for letter in line:
        dict[letter] = 1

print(sum)

