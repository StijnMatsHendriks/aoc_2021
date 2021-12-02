data = [line.strip("\n").split() for line in open("02.txt", "r").readlines()]

# challenge A
d = {"x": 0, "y": 0}

def translate(word, increment):   
    if word == "up":
        d["y"] -= int(increment)
    
    elif word == "down":
        d["y"] += int(increment)

    elif word == "forward":
        d["x"] += int(increment)


for command in data[:-1]:
    word = command[0]
    increment = command[1]    

    translate(word, increment)

answer = d["x"] * d["y"]
print(answer)

# challenge B
d = {"x": 0, "y": 0, "aim": 0}

def translate(word, increment):   
    if word == "up":
        d["aim"] -= int(increment)
    
    elif word == "down":
        d["aim"] += int(increment)

    elif word == "forward":
        d["x"] += int(increment)
        d["y"] += (d["aim"] * int(increment))

for command in data[:-1]:
    word = command[0]
    increment = command[1]

    translate(word, increment)

answer = d["x"] * d["y"]
print(answer)