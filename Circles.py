import pygame
import time

#[(60,60),(120,60),(180,60),(240,60),(300,60),(360,60)]
A=[(360, 60)]
B=[(300, 60)]
C=[(300, 60), (360, 60)]
D=[(240, 60)]
E=[(240, 60), (360, 60)]
F=[(240, 60), (300, 60)]
G=[(240, 60), (300, 60), (360, 60)]
H=[(180, 60)]
Word=[A, C, A, B]
white=(255, 255, 255)
black=(0, 0, 0,)
grey=(50, 50, 50)
screen1=pygame.display.set_mode((640, 120))
pygame.display.set_caption("Das Kapital")
screen1.fill(grey)
for letter in Word:
    position = letter
    print(letter)
    for x in position:
        print(x)
        pygame.draw.circle(screen1, white, x, 25)
        pygame.display.update()
        print("xloop")
        time.sleep(1)
    screen1.fill(grey)
    print("letterloop")
input("End of File")
