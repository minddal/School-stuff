'''
Created on 27/11/2012

@author: Andreas M
'''
thisLine = 'string'
ferielist = []
myFile = open("ferieplan2013+14.txt", encoding="utf-8")

for thisLine in myFile.readlines():
    if (thisLine.find("Ferieplan") == -1):
        print(thisLine)
        #ferielist.append(thisLine.strip("\n")
    else:
        print("")