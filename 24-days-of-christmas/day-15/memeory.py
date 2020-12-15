import time
start_time = time.time()



input = [0,3,1,6,7,5]

numbers = {}
for i in range(len(input)): numbers[input[i]] = i + 1

i = len(input)
last_number = input[-1]
while i <= 30000000 - 1:
    if last_number in numbers:
        temp = last_number
        last_number = i - numbers[last_number]
        numbers[temp] = i
    else:
        numbers[last_number] = i
        last_number = 0
    
    i += 1

print("Last:", last_number)
print("--- %s seconds ---" % (time.time() - start_time))