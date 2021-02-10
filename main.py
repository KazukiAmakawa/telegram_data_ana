#============================================================
#
# Check these parameter before you run the project
#
#
#============================================================

#LOCATION = "/Users/kazukiamakawa/Downloads/Telegram Desktop/ChatExport_2021-02-10 (3)"
LOCATION = "/Users/kazukiamakawa/Downloads/Telegram Desktop/ChatExport_2021-02-10"
# Location you saved your export chat files

FILETITLE = "messages"
# Filename of conversation html

INTERVAL = [1, 46]
# Messages you want to statistic

#START_DAY = 20191101
START_DAY = 20201201
# Start day of statistic int(YMD)

END_DAY = 20210301
# End day of statistic int(YMD)
#============================================================


import time 
import Init
import datetime 
import matplotlib.pyplot as plt 
from matplotlib.dates import drange 
import numpy as np 
import re
import os


start_time = [START_DAY % 100, int(START_DAY % 10000 / 100), int(START_DAY / 10000)]
end_time = [END_DAY % 100, int(END_DAY % 10000 / 100), int(END_DAY / 10000)]
date1 = datetime.datetime(start_time[2], start_time[1], start_time[0]) 
date2 = datetime.datetime(end_time[2], end_time[1], end_time[0] + 1) 
delta = datetime.timedelta(hours = 24) 
dates = drange(date1, date2, delta) 


current = START_DAY
time_stack_1 = []
while 1:
    day = str(int(current % 100))
    if len(day) == 1:
        day = "0" + day
    mouth = str(int((current % 10000) / 100))
    if len(mouth) == 1:
        mouth = "0" + mouth
    year = str(int(current / 10000))
    str_new = day + "." + mouth + "." + year
    time_stack_1.append(str_new)
    print(str_new, end = "\r")

    
    if current == END_DAY:
        break
    current = Init.GetNextDay(current, 1)
print()


val_stack = [0 for n in range(len(time_stack_1))]
for i in range(INTERVAL[0], INTERVAL[1] + 1):
    FileName = FILETITLE
    if i == 1:
        FileName += ""
    else:
        FileName += str(i)
    FileName += ".html"
    FileName = os.path.join(LOCATION, FileName)
    File = open(FileName, "r")
    print(FileName)
    while 1:
        line = File.readline()
        if not line:
            break
        val = ()
        try:
            val = re.search('<div class="pull_right date details" title="', line).span()
        except AttributeError:
            continue
        else:
            print(line[val[1]: val[1] + 10], end = "\r")
            for i in range(0, len(time_stack_1)):
                if time_stack_1[i] == line[val[1]: val[1] + 10]:
                    val_stack[i] += 1
                    break

    print()        

y = np.arange(len(dates)) 
   
plt.plot_date(dates, np.array(val_stack), "g")
#plt.title('matplotlib.pyplot.plot_date() function Example', fontweight ="bold") 
plt.show() 
