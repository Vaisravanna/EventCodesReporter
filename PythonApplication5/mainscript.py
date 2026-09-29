def analyze_events(code):
    CommonEvent = 0
    ConErrEve = 0
    ResNotFound = 0
    CriticalErrCount = 0
    UnkEve = 0

    CommonEveCodes = [200]
    ConErrCodes = [401,403]
    ResNotFoundCodes = [404]
    CriticalErrCodes = [500,503]

    for i in code:
        for j in CommonEveCodes:
            if i == j:
                CommonEvent+=1
         for j in ConErrCodes:
            if i == j:
                ConErrCodes+=1
         for i in ResNotFoundCodes:
             if i == j:
                 ResNotFoundCodes+=1
          for i in CriticalErrCodes:
              if i == j:
                  CriticalErrCodes+=1
        

    return CommonEvent, ConErrEve, ResNotFound, CriticalErrCount, UnkEve


def StatusAnalyzer(errors):
    if 0 <= errors <= 2:
        return "Стабильно"
    elif 3 <= errors <= 5:
        return "Внимание"
    else:
        return "Критично"


def ReportPrinter(CommonEvent, ConErrEve, ResNotFound, CriticalErrCount, UnkEve):
    total = CommonEvent + ConErrEve + ResNotFound + CriticalErrCount + UnkEve
    print(" Количество событий: ", total,
          "\n Количество нормальных событий: ", CommonEvent,
          "\n Количество проблем доступа: ", ConErrEve,
          "\n Количество проблем нахождения ресурса: ", ResNotFound,
          "\n Количество критических серверных ошибок: ", CriticalErrCount,
          "\n Количество неизвестных событий: ", UnkEve)


def main():
    codes = list(map(int, input().split()))

    CommonEvent, ConErrEve, ResNotFound, CriticalErrCount, UnkEve = analyze_events(codes)
    status = StatusAnalyzer(CriticalErrCount)
    ReportPrinter(CommonEvent, ConErrEve, ResNotFound, CriticalErrCount, UnkEve)
    print("Статус:", status)


main()