import numpy as np

data = [line.strip("\n").split(" -> ") for line in open('05.txt', 'r').readlines()]
data = [(int(coord.split(",")[0]), int(coord.split(",")[1])) for line in data for coord in line]
data = [[data[i], data[i+1]] for i in range(len(data)) if i % 2 == 0]

def check_if_usable(data):
    new_data = []
    
    for line in data:
        xa, ya = line[0]
        xb, yb = line[1]
        
        if (xa == xb) or (ya == yb):
            new_data.append(line)
    return new_data

def generate_points_from_line(data):
    new_data = []
    x_diag = []
    y_diag = []

    for line in data:
        xa, ya = line[0]
        xb, yb = line[1]

        if xa == xb:
            for y_coord in range(min(ya, yb), max(ya, yb)+1):
                new_data.append((xa, y_coord))
        if ya == yb:
            for x_coord in range(min(xa, xb), max(xa, xb)+1):
                new_data.append((x_coord, ya))
    return new_data

def generate_points_from_coords(data):
    new_data = []
    x_coords = []
    y_coords = []
        

    for line in data:
        xa, ya = line[0]
        xb, yb = line[1]
        diags = []

        if abs(xa-xb) == abs(ya-yb):
            for y_coord in range(min(ya, yb), max(ya, yb)+1):
                y_coords.append(y_coord)
            if ya > yb:
                y_coords = y_coords[::-1]
            print(y_coords)
            
            for x_coord in range(min(xa, xb), max(xa, xb)+1):
                x_coords.append(x_coord)
            if xa > xb:
                x_coords = x_coords[::-1]
            print(x_coords)
            diags = [(x_coords[i], y_coords[i]) for i in range(len(x_coords))]           
    return diags



field = np.zeros((999, 999))
data = check_if_usable(data)
# print(data)
# x_data = [[(9, 7), (7,9)], [(1,1), (3,3)]]
# x_data = generate_points_from_coords(x_data)
# print(x_data)

line_data = generate_points_from_line(data)
diag_data = generate_points_from_coords(data)

for coord in line_data:
    field[coord] += 1

for coord in diag_data:
    print(coord)
    field[coord] += 1

x, y = np.where(field > 1)
print(len(x))
