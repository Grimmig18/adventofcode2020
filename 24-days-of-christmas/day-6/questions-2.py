file = open('input.txt', 'r')
lines = file.readlines()

total = 0
dict = {}
group_size = 0

for line in lines:
    line = line.replace('\n', '')

    # End of group
    if line == '':
        total += sum(1 for key in dict if dict[key] == group_size)
        dict = {}
        group_size = 0
        # next group
        continue
    
    group_size += 1

    for letter in line:
        dict[letter] = dict[letter] + 1 if letter in dict else 1

print(total)
