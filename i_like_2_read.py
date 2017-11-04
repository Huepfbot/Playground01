import msvcrt
import time

def kbfunc():
    x = msvcrt.kbhit()
    if x:
        ret = ord(msvcrt.getch())
    else:
        ret = 0
    return ret


cnt = 0
while 1:
    cnt = cnt + 1
    print(cnt)
    k = kbfunc()
    if k != 0:
        print(k)
        time.sleep(2)
        cnt = int(cnt / 2) #gives nasty floating points without int()
        if k == 97:
            print("A has been pressed!")
            time.sleep(1)