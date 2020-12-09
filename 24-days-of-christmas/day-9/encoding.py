file = open('input.txt', 'r')
lines = file.readlines()

numbers = []
skip = 25

for line in lines: numbers.append(int(line))


for i in range(skip, len(numbers)):
    found = False

    for number in numbers[i-skip:i]:
        if numbers[i] - number in numbers[i-skip:i]:
            found = True
            break

    if found == False:
        print(i, numbers[i])
        break

