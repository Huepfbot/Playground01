import time
input_text=open("Kaputtal.txt","r")#How to open in binary, read/write etc? RESOLVED: Flag needs to be a STRING!
firstread=input_text.read(1)
print(firstread)
g=len(input_text)
for i in range(g):
    read=input_text.read(1)
    print(i, read)
    time.sleep(2)
input_text.close()
print("file closed:", input_text.closed)