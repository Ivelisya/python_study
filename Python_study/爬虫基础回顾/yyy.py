import pandas as pd
pf = pd.read_csv(r'D:\smzy\爬虫基础回顾\1.csv')
print(pf)

# pprint
# 可以让打印的数据有序排列
# 加上width参数


# 重写scrapy中的start_project
# 在程序一开始时调用
# 所以在scarpy中请求会被过滤
# 使用dont_filter
# 通过计算sha1
# 相同的请求对象算出来的sha1相同
def start_requests(self):
    yield
# scrapy帮你完成了requests.get()