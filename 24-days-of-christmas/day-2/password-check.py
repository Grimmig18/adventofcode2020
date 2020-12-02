# relative paths don't work?!
file = open('E:\\Projekte\\2020\\adventofcode2020\\24-days-of-christmas\\day-2\\input.txt', 'r') 
lines = file.readlines()

total_right = len(lines)

for line in lines:
    # Parse 
    temp = line.split(": ")
    lower = int(temp[0].split(" ")[0].split("-")[0])
    upper = int(temp[0].split(" ")[0].split("-")[1])
    letter = temp[0].split(" ")[1]
    password = temp[1]

    # Check rule
    count = password.count(letter)
    if count < lower or count > upper:
        total_right -= 1
    
print(total_right)