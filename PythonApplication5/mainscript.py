def analyze_events(code):
    CommonEvent = 0
    ConErrEve = 0
    ResNotFound = 0
    CriticalErrCount = 0
    UnkEve = 0
    UnkEveList = []
    UnknownEveLine = ""

    CommonEveCodes = [200]
    ConErrCodes = [401,403]
    ResNotFoundCodes = [404]
    CriticalErrCodes = [500,503]
    AllEveCodes = [200,401,403,404,500,503]

    for i in code:
        for j in CommonEveCodes:
            if i == j:
                CommonEvent+=1
        for j in ConErrCodes:
            if i == j:
                ConErrEve+=1
        for j in ResNotFoundCodes:
            if i == j:
                ResNotFound+=1
        for j in CriticalErrCodes:
            if i == j:
                  CriticalErrCount+=1
        for j in AllEveCodes:
            if i == j:
                break
            else:
                UnknownEveLine = UnknownEveLine+" "+str(i)  
                UnkEve+=1
                break
                
    UnkEveList = list(map(str,UnknownEveLine.split()))
    return CommonEvent, ConErrEve, ResNotFound, CriticalErrCount, UnkEve, UnkEveList

def StatusAnalyzer(errors):
    if 0 <= errors <= 2:
        return "Стабильно"
    elif 3 <= errors <= 5:
        return "Внимание"
    else:
        return "Критично"

def ReportPrinter(CommonEvent, ConErrEve, ResNotFound, CriticalErrCount, UnkEve, UnkEveList, status):
    total = CommonEvent + ConErrEve + ResNotFound + CriticalErrCount + UnkEve

    print(" Количество событий: ", total,
          "\n Количество нормальных событий: ", CommonEvent,
          "\n Количество проблем доступа: ", ConErrEve,
          "\n Количество проблем нахождения ресурса: ", ResNotFound,
          "\n Количество критических серверных ошибок: ", CriticalErrCount,
          "\n Количество неизвестных событий: ", UnkEve,
          "\n Статус: ", status,
          "\n Номера неизвестных событий: ")

    for i in UnkEveList:
        print(i)

def main():
    codes = list(map(int, input().split()))
    CommonEvent, ConErrEve, ResNotFound, CriticalErrCount, UnkEve, UnkEveList = analyze_events(codes)
    ReportPrinter(CommonEvent, ConErrEve, ResNotFound, CriticalErrCount, UnkEve, UnkEveList,status = StatusAnalyzer(CriticalErrCount))

main()