from bs4 import BeautifulSoup
# city_list = []
ALL_DATA = []
# 获取城市信息
with open('C:\\Users\\20212\\smzy\\爬虫\\beautifulsoup\\素材\\匹配天气.html','r',encoding='UTF-8') as fp:
    soup = BeautifulSoup(fp,'lxml')
#     city = soup.find('dd')
#     city_gener = city.stripped_strings
#     for i in city_gener:
#         city_list.append(i)
#     city_out = soup.select('div [class="w_city city_guonei gj"]>dl>dd[class="jind"]>a')
#     for a in city_out:
#         city_list.append(a.get_text())
# print(city_list)
# 获取天气信息
    conMidtab = soup.find('div',class_='conMidtab')
    tables = conMidtab.find_all('table')
for table in tables:
    # 过滤掉标题行
    trs = table.find_all('tr')[2:]
    for index, tr in enumerate(trs):
        tds = tr.find_all('td')
        # print(index, tds)
        # 获取城市和天气
        city_td = tds[0]
        temp_td = tds[3]
        # 过滤掉表格左侧的省/直辖市
        if index == 0:
            city_td = tds[1]
            temp_td = tds[4]
        city_td = list(city_td.stripped_strings)[0]
        temp_td = list(temp_td.stripped_strings)[0]
        ALL_DATA.append({'city':city_td,'temp':temp_td})

print(ALL_DATA)
    

    



