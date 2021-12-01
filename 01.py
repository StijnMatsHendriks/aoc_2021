data = [int(line.strip("\n")) for line in open("01.txt").readlines()]

# challenge A
def scan(a_list, i):
    return int(a_list[i] > a_list[i-1])

amount = 0
for i in range(len(data)):
    amount += scan(data, i)

print(amount)

# challenge B
def scan_sweep(a_list, i):
    i_depth = sum(a_list[i:i+3])
    j = i+1
    j_depth = sum(a_list[j:j+3])
    return int(j_depth > i_depth)

amount = 0
for i in range(0, len(data)-3):
    amount += scan_sweep(data, i)

print(amount)
    