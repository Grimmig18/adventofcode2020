from operator import xor

# relative paths don't work?!
file = open('input.txt', 'r') 
lines = file.readlines()

total_right = len(lines)

for line in lines:
    # Parse 
    temp = line.split(": ")
    pos_1 = int(temp[0].split(" ")[0].split("-")[0])
    pos_2 = int(temp[0].split(" ")[0].split("-")[1])
    letter = temp[0].split(" ")[1]
    password = temp[1]

    # Check rule
    if xor(password[pos_1 - 1] == letter, password[pos_2 - 1] == letter) == False:
        total_right -= 1
    
print(total_right)