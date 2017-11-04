import msvcrt
import time

#_init_
s="ini"
k="ini"
#ready state

while s!=115:
    print("press left button, s")
    #s=msvcrt.kbhit()
    s=ord(msvcrt.getch())
    #time.sleep(1)
while k !=107:
    print("press right button, k")
    k=ord(msvcrt.getch())
    #time.sleep(1)
for cntdwn in range(5,1,-1):
    print(" test begins in ", cntdwn, " seconds.")
    time.sleep(1)
#main loop