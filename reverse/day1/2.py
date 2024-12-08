import execjs
import subprocess
from functools import partial   # 用于将函数的某些参数固定下来，返回一个新函数
subprocess.Popen = partial(subprocess.Popen,encoding = 'utf-8')
s = """function fn(){
       return{
        name : 'smzy',
        age : 18,
        like : ['python','javascript','java'],
        hobby : {ability : 'coding'}
        };
    }
    
"""


import execjs
js = execjs.compile(s)
r = js.call('fn')
print(r)
