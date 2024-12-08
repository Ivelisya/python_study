# 调用 my.js当中的fn函数
# 在引入execjs之前
import subprocess
from functools import partial   # 用于将函数的某些参数固定下来，返回一个新函数
subprocess.Popen = partial(subprocess.Popen,encoding = 'utf-8')
import execjs
f = open('my.js', 'r', encoding='utf-8')
all_js_code = f.read()
js = execjs.compile(all_js_code)
r = js.call('fn', 'hello_world')
for item in r:
    print(item)
f.close()