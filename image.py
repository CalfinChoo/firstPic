f = open("image.ppm", "w+");
width = 496
height = 496
f.write("P3\n{} {}\n255\n".format(width, height))

sqSize = int(width/8)
swap = False
targets = [(133, 94, 66), (222, 184, 135)]

def fold(val):
    if (val > width / 2): val = width - val
    return val

def calcColor(x, y):
    return int((width/2 - (fold(x) + fold(y)) / 2) - 66)

for y in range(height):
    for x in range(width):
        if (swap): f.write("{} {} {} ".format(str(targets[0][0] + calcColor(x, y)), str(targets[0][1] + calcColor(x, y)), str(targets[0][2] + calcColor(x, y))))
        else: f.write("{} {} {} ".format(str(targets[1][0] + calcColor(x, y)), str(targets[1][1] + calcColor(x, y)), str(targets[1][2] + calcColor(x, y))))
        if ((x + 1) % sqSize == 0 and swap == False): swap = True
        elif ((x + 1) % sqSize == 0 and swap == True): swap = False
    if ((y + 1) % sqSize == 0 and swap == False): swap = True
    elif ((y + 1) % sqSize == 0 and swap == True): swap = False
    f.write("\n")
f.close()
#Draws a gradient chessboard
