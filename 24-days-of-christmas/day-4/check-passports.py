file = open('input.txt', 'r')
lines = file.readlines()

req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
current_passport = ''
valids = 0
counter = 0

for line in lines:
    counter += 1
    if len(line) > 1:
        # No empty line, add to passport info
        current_passport += line
    else:
        # Potentially valid
        valids += 1
        # Empty line -> Evaluate current passport and reset
        current_passport = current_passport.replace('\n', ' ').replace('\r', '')
        pairs = current_passport.split(' ')
        keys = [pairs[i].split(':')[0] for i in range(len(pairs))]
        
        if counter > 1061:
            print(current_passport)
            print(keys)

        # Check if req_fields are missing
        for req in req_fields:
            if req not in keys:
                valids -= 1
                break

        current_passport = ''

print(valids)