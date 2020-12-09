import numpy as np

file = open('input.txt', 'r')
lines = file.readlines()

numbers = []
skip = 25
weakness = -1
weakness_index = -1

for line in lines: numbers.append(int(line))

for i in range(skip, len(numbers)):
    found = False

    for number in numbers[i-skip:i]:
        if numbers[i] - number in numbers[i-skip:i]:
            found = True
            break

    if found == False:
        print("Weakness Found:", i, numbers[i])
        weakness = numbers[i]
        weakness_index = i   
        break


# Find set
for i in range(0, len(numbers)):
    j = i + 2
    while np.sum(numbers[i:j]) <= weakness:
        # print(np.sum(numbers[i:j]))
        if np.sum(numbers[i:j]) == weakness:
            print(numbers[i:j])
            print(i, j-1, numbers[i], numbers[j-1], max(numbers[i:j]) + min(numbers[i:j]))
            break
        j += 1
