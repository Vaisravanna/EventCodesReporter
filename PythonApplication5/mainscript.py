def analyze_events(code):
    CommonEvent = 0
    ConErrEve = 0
    ResNotFound = 0
    CriticalErrCount = 0
    UnkEve = 0

    for i in code:
        if i == 200:
            CommonEvent += 1
        elif i == 401 or i == 403:
            ConErrEve += 1
        elif i == 404:
            ResNotFound += 1
        elif i == 500 or i == 503:
            CriticalErrCount += 1
        else:
            UnkEve += 1

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