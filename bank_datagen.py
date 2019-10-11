# Bank Data generator
# Author: Jagadish Rao

import fileinput
import random

filnum = input("What is the file number: ")

datareccount = int(input("How many data records:"))

filnam =  "C:\\pyproj\\largedata\\data" + filnum + ".csv"
datarec = ""


fil = open(filnam, "a")

datarec = "Id,name,last,balance,acc type\n"                 # header record
fil.write(datarec)

for i in range(datareccount):
    datarec = str(i + 1) + ",FName" + filnum + str(i + 1) + ",LName" + filnum + str(i + 1) + "," + str(random.randint(1, 100000))
    if random.random() > 0.5:
        datarec = datarec + ",saving\n"
    else:
        datarec = datarec + ",checking\n"

    fil.write(datarec)                                      # data record


fil.close()

print ("created data file")

