import requests
import re
headers = {
    "Cookie": "MUID=228DFE2F0EE96CFF20EEEDC00AE96A50; MUIDB=228DFE2F0EE96CFF20EEEDC00AE96A50; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=6E747C86F6C545709D19E6F7283C02E1&dmnchg=1; ANON=A=A1E05A8DCDAA1697F36593F6FFFFFFFF&E=1d33&W=1; NAP=V=1.9&E=1cd9&C=VPawWfqFvKJNjVfVg2x21lKelnN6Kj89r1aiX1pDf6a9JmVZdnVMvg&W=1; PPLState=1; USRLOC=HS=1&ELOC=LAT=30.06017303466797|LON=112.21394348144531|N=Gongan%20County%2C%20Hubei|ELT=10|; _RwBf=r=0&ilt=2&ihpd=0&ispd=2&rc=1572&rb=1572&gb=0&rg=0&pc=1551&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=1&l=2024-02-25T08:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&ard=0001-01-01T00:00:00.0000000&o=0&p=BINGCOPILOTWAITLIST&c=MR000T&t=8790&s=2023-06-26T13:15:42.5396827+00:00&ts=2024-02-26T07:05:58.6084804+00:00&rwred=0&wls=2&wlb=0&wle=0&ccp=0&lka=0&lkt=0&aad=0&TH=&mta=0&e=uF0e1Aigj1js8D4gk87p-YCzFyp5cEcUXnjl2RJIuKohD-G_g519Wzp36e509HMZTyBW41gtzutlMV_24zwS9w&A=&rwdbt=2024-01-02T05:08:10.5733113-08:00&rwflt=2023-06-27T09:29:28.2018828-07:00; KievRPSSecAuth=FABSBBRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACMn+Vh9TePq+EAQIdyjqE2gt9L3okDFddnyVSxscqIbSuOhXUfvpNDzJRFDQfpma7JpmYs2S0wAYY9++ZhUPDce9W1vUYtIDn3rt4Rh9NR+AQQTsXVdF/fcroSH5HvANqWLxREyPV1ypsrROidaZSfBBLBIT3hhw3w0eJNlT1o2YTzkmFoG7StHNKens9gCLq8gKadkxPjQX3SD1tcv2h0KzWam5NxovJToD+Id9FW4NN9f8nPeSp2OuD/ssKjT331jA5PP1oW3lx7M7LG3AmfXE/d1eLhPJyr3gXM+TBj9aF51kT6rcLcMkzw5L/ZcSVO+5iKmacxHj3QAbDiVKG+ftv9YRVHAQqzyKToKfvhcn9XNgm1VrCsSCKxsntixMs/AqKWzqmI/id70vFzhQf/WmmJflFHxRmDfShTI0bNobAgxSJg3TIlRVepUqQjS8nq75ytUSxRcCDyAF6pbGaEcdFCWfpRawdEVe+jiiNx7oCCwmLPP0DCTWb++XyXAswzmd30Tj096vlYnG07cJ3dGnonVDtaGLT7IQ16YUD2n3KBOeXmE0EmvPXX1w47Xv1riIDea5COS5wB0H3vyIN7EbFe6vhFwblYFcLxov6RUzDu/mmXlR6/WTyeKwHyS8gWA8xk5+IiN+5DMnPcNcyfwCb3Ju6wk+WeuKJo3NQYWFChKax8dFuS+MRdjxKlMkeYNh8RhXWsDOs0TdEDPMiaBEnpGJ9+1vp++Fcx59gvu//Tr5YBKXQVFhd++xPGTZXyTuU69JBOrKClVf0Bp+ueAXIrcKA1PIC4cPLIQZOmZxsORiFkVQUzv6wjIm6RNKFk8LIfxAPk3RYuunspyCp7jhmVuOqBcbnOEYl8paNC5ycllSrYeMNSSQ5oaQGuyrWp0X42bHDN3e02ujCHg7o53TP6dbnm30nE4p2nPF+8wDNQPPuINLu/5pqg2XX46Vnjmeu62qi+eWYoUsI+PKDzze15QuJwTfQ4OLHdp6mgUQe+TIvquOCjgb0+MfoCr60xleYfV3oI7GwZyhhuMZXVIV3kIKzxhcI8033Y+C7SOk/VxswIt+PIKts8ZGy+lYORSBU9yrB5Yn9icB/EmCMWgYgrbnnCRLCni1xSFMyhVQ5nUOtOZ/Yg/qTEHnT4dm2GZXn97V2kIvOC+v319ex1/DZvKps8H3z/Cevyxcyr0bPkqb8u3kw5bqE2FDBh8RZqg+sWAvdrpLVKQGnNWyIL93aaGJCakO2Nkf0hMH8OmD7Am5XSkcEHSqQ53STXuYALymnj6csv697v7ITvfoHiNhARewAi5SXtlgtjbDVdwArdd0rhkSMHRQQCF+OWWqLcPfniueVD1C5ziAvlOifD+5y4g9TaJLhqwccgk+qaPF4cmBNiwJzKZgxxQAfQGAqnTYqdpb9ZsBMa+KdaXBf0Y=; _U=1gXAzHVsIOp4yGxjzTXVrYGjmckQWbf38md7Is1uaddZteS_DCBxykRunnQ5BBw7ltqX9KaT8chWjyy5znMmVmI41k1lkn2qk9KlJrnkFjHsuMVIGQN53BxTZxcSTXxc7RvoyC-FKKnggwErNcSloUwwa8OHq6mgsHfgOZvy0mbB8hossEoGxoBu6eE8PLvboni-BdCKgsMuZ9lsxOXO7sQ; _EDGE_S=SID=3678E14E4A7B6FD326C2F57D4BDA6E4B&mkt=zh-CN; WLS=C=69ef7b22eca15137&N=ma; _SS=SID=3678E14E4A7B6FD326C2F57D4BDA6E4B; _tarLang=default=zh-Hans; _TTSS_OUT=hist=WyJlbiIsImx6aCIsInpoLUhhbnMiXQ==; btstkn=qQxfpyIZu6wahQCYuh6gES%252FdnqlWJx1Ga9KsyaRaS3SQDPVkupv60EOiw9syOY3gCLsFiuj6%252BwEV554csBM8wOrzHY6stLRi0OTTl4q7CQs%253D; SRCHUSR=DOB=20240101&T=1709141123000&TPC=1709137080000&POEX=W; SRCHHPGUSR=SRCHLANG=en&BRW=W&BRH=M&CW=1440&CH=731&SCW=1423&SCH=1961&DPR=2.0&UTC=480&DM=1&PV=15.0.0&CIBV=1.1381.12&HV=1709141127&WTS=63844527955&BZA=0&PRVCW=1046&PRVCH=746; _TTSS_IN=isADRU=1&hist=WyJlbiIsImF1dG8tZGV0ZWN0Il0=; ipv6=hit=1709144731219&t=4",
    "Origin": "https://www.bing.com",
    "Referer": "https://www.bing.com/translator?ref=TThis&from=&to=zh-Hans&isTTRefreshQuery=1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
word = input('请输入要翻译的英语：')
c = False
if word:
    c = True
    word = word
else:
    word = input('请输入要翻译的英语：')
    while not word:
        print('请输入要翻译的英语!!!')
        word = input('请输入要翻译的英语：')
    c = True
data = {
    "fromLang": "auto-detect",
    "to": "zh-Hans",
    "token": "A4ae5JsjzsQ3eNuUyJY9GobLXNb3afRJ",
    "key": "1709148390719",
    "text": word,
    "tryFetchingGenderDebiasedTranslations": True
}

def get_translation():
    url = "https://www.bing.com/ttranslatev3?isVertical=1&&IG=71E81440F7F241AB9B11E57F105336B2&IID=translator.5025"
    resp = requests.post(url, headers=headers, data=data)
    # print(resp.text)
    # exit()
    a = resp.json()[0]['translations'][0]['text']
    return a
def get_all_translation(word,a):
    new_data = {
    "from": "en",
    "to": "zh-Hans",
    "text": word,
    "translatedText": a,
    "token": "A4ae5JsjzsQ3eNuUyJY9GobLXNb3afRJ",
    "key": "1709148390719"
}
    headers['Origin'] = 'https://www.bing.com'
    headers['Referer'] = 'https://www.bing.com/translator?'
    url = "https://www.bing.com/tlookupv3?isVertical=1&&IG=71E81440F7F241AB9B11E57F105336B2&IID=translator.5022.3"
    resp = requests.post(url, headers=headers, data=new_data)
    b = resp.json()
    translate = re.findall(r"'normalizedTarget':\s*'([^']*)'", str(b))
    # print(str(b))
    return translate
    # print(resp.text)
translate = get_translation()
all_translate = get_all_translation(word,translate)
length = len(all_translate)
print('共有{}种翻译'.format(length))
print('全部翻译如下：')
for index,i in enumerate(all_translate):
    index += 1
    if index == length:
        print(i)
    else:
        print(i, end='、')