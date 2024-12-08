import requests
url = 'https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=535489&size=15'
proxy = {
    'http':'http://121.37.207.154:8999'
}
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69',
    'Cookie':'acw_tc=276077b516938071674351323e708229efaf4ff52a89557eb8214e8351ac56; xq_a_token=a0f5e0d91bc0846f43452e89ae79e08167c42068; xqat=a0f5e0d91bc0846f43452e89ae79e08167c42068; xq_r_token=76ed99965d5bffa08531a6a47501f096f61108e8; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTY5NTUxNTc5NCwiY3RtIjoxNjkzODA3MTQ4ODI2LCJjaWQiOiJkOWQwbjRBWnVwIn0.jBfNncrLdyIi0rl-iOEtz27UUI4gX-n1NUyCTBkP7oCRLp9ufRVljuJB4STh8TYIvCvJ0gAKLh8NrAJfW-E3DTTZxPSGeMo0uTxmza7NHCgbE3TMSuYKSbR4LQBJudNlFdDj6ppik6xP4MQHLe6tHE0QbZ4HSmvAq2J48aV43D93NhvaxrAU34_wjeF6KRXA2yYNukdiOzwxKZKFgeyt0oYy-MP7FfmmWRz8GYTH9G0VOJs8vNqZBRYKMcJD96wJfcWeJj4hR6gORB5WbdaN3x-Tzk2al1CwIRhPkPmn0mNj6wfZkzWQOIsGTakl2XXGLbhM9Nwk2cJbPKlxVbK7OA; cookiesu=791693807167488; u=791693807167488; device_id=aed422c019cc2e5c575aa4ac9d2ce280; Hm_lvt_1db88642e346389874251b5a1eded6e3=1693807170; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1693807755'

}
res = requests.get(url,headers=header,proxies=proxy)
print(res.content.decode())