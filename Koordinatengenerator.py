#Koordinatengenerator. A small supportroutine for upcoming adventures in Pygame.draw.functions.
#User enters Grid(i.e: screen) dimensions and desired space between coordinates.
#The Tool then spits out a List of Coordinates
#To do: -Get the Routine running
#       -display coordinates in a fashion matching their physical position
#       -output the List to a .csv file\
#       -output the List to a .json file
#how to directly enter this as a tuple? "enter dimensions: 640x320 -> (640;320)
#dim_x, dim_y = int(input("screen dimensions?"))
dim_x = int(input("screen width?"))
dim_y = int(input("screen height?"))
step_size = int(input("step size?"))
x = 0
y = 0
while y <= dim_y:
    while x <= dim_x:
        print(x, y)
        x = x + step_size
    x = 0
    y = y + step_size
print(23*"-YaY-")
