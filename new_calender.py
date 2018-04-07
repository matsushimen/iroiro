import sys
args = sys.argv
daysinYear = int(args[1])
daysinMonth = int(args[2])
daysinWeek = int(args[3])
date = args[4]
date_info = []
day = [chr(i) for i in range(65,65+26)]
 
for i in date.split("-"):
    date_info.append(int(i))
if(date_info[2]>daysinMonth):
    print(-1)
    exit(0)

totaldays = 0
uruMonth = 0
uru_safe = 0
if(date_info[1]>daysinYear//daysinMonth):
    uru_safe = 1
for i in range(1,date_info[0]+1):
    uruMonth += daysinYear%daysinMonth
    if(uruMonth>=daysinMonth):
        if((date_info[1]==daysinYear//daysinMonth+1)&(date_info[0]==i)):
            uru_safe = 0
        uruMonth -= daysinMonth
if(uru_safe==1):
    print(-1)
    exit(0)

totaldays = 0
uruMonth = 0
for i in range(1,date_info[0]):
    totaldays += daysinYear
    uruMonth += daysinYear%daysinMonth
    if(uruMonth>=daysinMonth):
        totaldays += daysinMonth
        uruMonth -= daysinMonth

totaldays += daysinMonth*(date_info[1]-1)+date_info[0]
print(day[totaldays%daysinWeek-1])
