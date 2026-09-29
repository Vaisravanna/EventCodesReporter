codes = list(map(int,input().split()))
CommonEvent = 0
ConErrEve = 0
ResNotFound = 0
CriticalErrCount = 0
UnkEve = 0
def analyze_events(codses)
for i in codes:
    if (i==200):
            CommonEvent=+1
    elif(i==401 or i==403):
            ConErrEve=+1
    elif(i==404):
            ResNotFound=+1
    elif(i==500 or i==503):
            CriticalErrCount=+1
    else:
        UnkEve=+1
        return()
def отчет()
    print(" Количество событий: ", CommonEvent+ConErrEve+ResNotFound+CriticalErrCount+UnkEve,"\n Количество нормальных событий: ", CommonEvent, "\n Колличество проблем доступа: ", ConErrEve,"\n Колличество проблем нахождения ресурса: ",ResNotFound,"\n Количество критических серверных ошибок: ",CriticalErrCount,"\n Количество неизвестных событий: ", UnkEve)
    return()