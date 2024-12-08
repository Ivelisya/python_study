#sha1,sha256,sha512都是hashlib中的模块
from hashlib import sha1, sha256, sha512
obj = sha1()
data = "smzy".encode("utf-8")
obj.update(data)
result = obj.hexdigest()
print(result)#35b23ca5c5995b070a2884d8ccb006dea8622f82