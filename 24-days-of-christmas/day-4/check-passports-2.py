import re

file = open('input2.txt', 'r')
lines = file.readlines()

req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
current_passport = ''
valids = 0

def validate(p):
    for req in req_fields:
        if req not in p:
            return False
    

    # pffffffffff
    if int(p['byr']) < 1920 or int(p['byr']) > 2002:
        return False
    
    if int(p['iyr']) < 2010 or int(p['iyr']) > 2020:
        return False

    if int(p['eyr']) < 2020 or int(p['eyr']) > 2030:
        return False

    hgt = p['hgt']
    if hgt[-2:] == 'cm':
        if int(hgt[0:-2]) < 150 or int(hgt[0:-2]) > 193:
            return False
        
    elif hgt[-2:] == 'in':
        if int(hgt[0:-2]) < 59 or int(hgt[0:-2]) > 76:
            return False
    else:
        return False

    if not re.compile('#[a-f0-9]{6}').match(p['hcl']):
        return False

    if p['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    if not re.compile('[0-9]{9}').match(p['pid']) or len(p['pid']) > 9:
        return False


for line in lines:
    if len(line) > 1:
        # No empty line, add to passport info
        current_passport += line
    else:
        # Potentially valid
        valids += 1
        # Empty line -> Evaluate current passport and reset
        current_passport = current_passport.replace(
            '\n', ' ').replace('\r', '')
        pairs = current_passport.split(' ')

        pairs_dict = {}
        for pair in pairs:
            pair = pair.split(':')
            pairs_dict[pair[0]] = pair[-1]

        # Check if req_fields are missing
        if validate(pairs_dict) == False:
            valids -= 1

        current_passport = ''

print(valids)