import requests
from bs4 import BeautifulSoup


def get_site(url):
    return requests.get(url)


def parse_teams(table):
    """Возвращает словарь Команда: Очки"""
    names = []
    teams = table.find("tbody").find_all("tr")
    result = {}
    temp = []
    for i in range(len(teams)):
        temp.append(teams[i].find_all("td"))
    for i in temp:
        names.append(i[-1].text)
    for i in teams:
        names.append(i.find("a").text)
    for i in range(len(names) // 2):
        result[names[i + len(names) // 2]] = names[i]
    r = 1
    for i in result.items():
        print(str(r) + ". " + i[0] + " (" + i[1] + ")")
        r += 1
    return result


def parse_dates(api, key=1):
    """Получает с сайта даты и названия турнира и отдает в управление в обертку-функцию"""
    result = BeautifulSoup(api.text, 'html.parser')
    dates = result.find_all("div", class_="stat mB6")
    temp, titles = [], []
    ret = {}
    new1, new2, res1, res2 = [], [], [], []
    titles = result.find_all("h3")
    for i in range(len(titles)):
        titles[i] = titles[i].text
    for i in range(len(dates)):
        temp.append(dates[i].find("tbody").find_all("tr"))

    for i in range(len(dates)):
        new1.append(dates[i].find_all("td", class_="name-td alLeft bordR"))
        new2.append(dates[i].find_all("td", class_="name-td alLeft"))

    for i in range(len(new1)):
        res1.append(new1[i][1].find("a").text)
        res1.append(new1[i][2].find("a").text)
        try:
            res2.append(new2[i][1].find("a").text)
        except:
            res2.append("-")
        try:
            res2.append(new2[i][2].find("a").text)
        except:
            res2.append("-")
    for i in range(len(res1)):
        ret[res1[i]] = res2[i]
    nice_wrapper_dates(titles, res1, res2, key)


def nice_wrapper_dates(titles, res1, res2, key=1):
    """Красивое оформление кода для дат"""
    kk = 0
    if key == 1:
        for i in range(len(titles)):
            print(titles[i])
            print(res1[kk] + " " + res2[kk])
            print(res1[kk + 1] + " " + res2[kk + 1])
            print('\n')
            kk += 2
    for i in range(len(res2)):
        if res2[i] == "-":
            print("Ближайший турнир - это" + f' "{titles[i // 2]}"' + " " + res1[i] + res1[i + 1])
            break


def main():
    print("----------------------------------")
    print("Для общих сведений дат введите 1")
    print("Для таблицы команд введите 2")
    print("Для таблицы личных зачетов введите 3")
    print("----------------------------------")
    scanner = input()
    if scanner == "1":
        url1 = 'https://www.sports.ru/f1-championship/calendar/'
        sc = input("Показать прошедшие матчи? n, если нет")
        api1 = get_site(url1)
        if api1.status_code == 200:
            if sc == "n":
                parse_dates(api1, 0)
            else:
                parse_dates(api1, 1)

    url1 = "https://www.sports.ru/f1-championship/table/"
    result = BeautifulSoup(api.text, 'html.parser')
    table = result.find_all("table", class_="stat-table table")
    if scanner == "2":
        teams = parse_teams(table[1])
    if scanner == "3":
        teams = parse_teams(table[0])


if __name__ == "__main__":
    main()