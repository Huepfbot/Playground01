from time import sleep
inputfile1=open("kaputtal.txt")
inputfile2=open("Wealthofnations.txt","rw")
outputname=input("name of outputfile")
outputfile=open(outputname,"rw")
readbit=inputfile1.read(10)
outputfile.write(readbit)
