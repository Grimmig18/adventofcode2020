file = open('input.txt')
lines = file.readlines()

plugs = []
used = []
for line in lines: plugs.append(int(line))
plugs.sort()
print(plugs)

ones = 1
threes = 1

for i in range(1, len(plugs)):
    if plugs[i] - plugs[i-1] == 3:
        threes += 1
    elif plugs[i] - plugs[i-1] == 1:
        ones += 1
    else:
        print("Das geht nicht")

print(ones, threes)


# def next_plug(jolts):
#     candidates = []
#     for plug in plugs:
#         if plug > jolts and plug <= jolts + 3:
#             candidates.append(plug)
#             used.append(plug)
#             return plug

# plug = 0
# adapter = plugs[-1]
# while plug < adapter - 3

