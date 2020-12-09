done_paths = []


class Counter:
    counter = 0
    @staticmethod
    def increase_counter(n):
        print(n)
        Counter.counter += n

def contains_gold(dict, start, golds):
    done_paths.append(start)

    for child in dict[start]:
        count = child[0]
        color = child[1]

        if color == 'shiny gold':
            golds = golds + 1
            print("Here")
        elif color not in done_paths:
            temp = contains_gold(dict, color, 0)
            print("Here: ", temp)
            golds += temp
            # print(golds)

    # print(golds)
    return golds
    

f = open('input.txt', 'r')
lines = f.readlines()

bag_dict = {}
# dict entry: {'plaid plum': [[5, 'muted yellow'], [2, 'dim crimson']]}

# parse data
for line in lines:
    line = line.replace('\n','')
    parent = line.split(' bags contain ')[0]
    # contains = line.split(' bags contain ')[1]
    contains = line.split(' bags contain ')[1].split(', ')

    if contains[0] == 'no other bags.':
        bag_dict[parent] = []
        continue

    children = []

    for child in contains:
        count = child.split(' ')[0]
        color = child.split(' ', 1)[1].split(' bag')[0]

        children.append([count, color])

    bag_dict[parent] = children

# print(bag_dict)

gold_count = 0
for color in bag_dict:

    if color not in done_paths:
        gold_count += contains_gold(bag_dict, color, golds=gold_count)

print(gold_count)
