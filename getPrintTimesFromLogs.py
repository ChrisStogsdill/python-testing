import os
from datetime import datetime

tempLogsDir = r"C:\Users\cstogsdill\Downloads\temp logs"

for file in os.listdir(tempLogsDir):
    with open(os.path.join(tempLogsDir, file), 'r') as f:
        readLines = f.readlines()
        counter = 0
        for line in readLines:
            if "Copying" in line:
                time1 = readLines[counter][11:18]
                time1Object = datetime.strptime(time1, '%H:%M:%S')
                time2 = readLines[counter+1][11:18]
                time2Object = datetime.strptime(time2, '%H:%M:%S')
                totalTime = time2Object - time1Object
                if totalTime.seconds > 5:
                    print (readLines[0].strip('\n\r'))
                    if "Counter Order" in readLines[25]:
                        print (readLines[25].strip('\n\r'))
                    print(readLines[counter].strip('\n\r'))
                    print(readLines[counter+1].strip('\n\r'))
                    print('time to copy ', time2Object - time1Object, '\n')
                
            counter += 1
    f.close()