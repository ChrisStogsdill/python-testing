from datetime import datetime

time1 = "09:59:59"
time2 = "10:00:00"

time1Object = datetime.strptime(time1, '%H:%M:%S')
time2Object = datetime.strptime(time2, '%H:%M:%S')

testTime = '06/21/2022 10:01:59'

print(testTime[10:19])