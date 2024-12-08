import requests
from lxml import etree
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.999 Safari/537.36"
}

# resp = requests.get("https://music.163.com/discover", headers=headers)
# print(resp.text)
# with open('D:\\smzy\\reverse\\day2\\网易.html', 'w', encoding='utf-8') as f:
#     f.write(resp.text)

# print('ok')
tree = etree.HTML(open('/reverse/day2/网易云/网易.html', 'r', encoding='utf-8').read())
li_list_ele = tree.xpath('//*[@id="top-flag"]/dl/dd/ol')
print(li_list_ele)
# a = 0
id = []
for li_list in li_list_ele:
    for li in li_list:
        # a += 1
        id.append(li.xpath("./div/a[1]/@data-res-id")[0])
