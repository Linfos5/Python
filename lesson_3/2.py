HttpCode = int(input("Введите http-код: "))

code1xx = HttpCode
code2xx = HttpCode
code3xx = HttpCode
code4xx = HttpCode
code5xx = HttpCode

match code1xx:
    case 100:
        print("Continue")
    case 102:
        print("Processing")
    case "103":
        print("Early Hints")    
    case _:
        print("Неизвестный код для группы 1xx")
            
match code2xx:
    case 200:
        print("OK")
    case 204:
        print("No Content")
    case _:
        print("Неизвестный код для группы 2xx")

match code3xx:
    case 302:
        print("Found")
    case 305:
        print("Use Proxy")
    case _:
        print("Неизвестный код для группы 3xx")
            
match code4xx:
    case 404:
        print("Not Found")
    case 409:
        print("Conflict")
    case _:
        print("Неизвестный код для группы 4xx")
            
match code5xx:
    case 503:
        print("Service Unavailable")
    case 510:
        print("Not Extended")
    case _:
        print("Неизвестный код для группы 5xx")
