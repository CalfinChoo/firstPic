f = open("image.ppm", "w+");
width = 496
height = 496
f.write("P3\n{} {}\n255\n".format(width, height))

sqSize = width/8
swap = False
for y in range(height):
    for x in range(width):
        for i in range(3):
            if (swap): f.write("222 184 135 ")
            else: f.write("180 207 250 ")
        if (x % sqSize == 0 and swap == False): swap = True
        elif (x % sqSize == 0 and swap == True): swap = False
    f.write("\n")
