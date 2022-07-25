import csv

file = open(r"C:\Users\cstogsdill\Downloads\phonelist.txt", "r")
csvFile = open(r"C:\Users\cstogsdill\Downloads\phonelist.csv", "w")
indexLocation = 0
outputDict = {}
csvColumns = ["Endpoint", "Contact"]
for line in file: 
    if line.strip() == "":
        indexLocation = indexLocation + 1
    
    lineArray = line.strip().split(":")
    if lineArray[0] == "Endpoint":
        outputDict[indexLocation] = {lineArray.pop(0) : lineArray}
    if lineArray[0] == "Contact":
        outputDict[indexLocation][lineArray.pop(0)] = lineArray
    
writer = csv.DictWriter(csvFile, fieldnames=csvColumns)
writer.writeheader()
for key in outputDict:
    writer.writerow(outputDict[key])

